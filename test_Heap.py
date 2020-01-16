import unittest
import Heap


class MyTestCase(unittest.TestCase):
    def test_arr12(self):
        heap = Heap.Heap()
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        arr = heap.MakeHeap(a, 3)
        count = 0
        for i in arr:
            if i !=None:
             count +=1
        self.assertEqual(len(a) == count, True, 'digits are incorrect')
        self.assertEqual(len(arr) == 15, True, 'None are incorrect')
        self.assertEqual(arr[0] == 12, True, 'first elem are incorrect')

    def test_correct_form(self):
        heap = Heap.Heap()
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        arr = heap.MakeHeap(a, 3)
        count = 0
        for i in range(len(arr)):
            if arr[i] != None and 2 * i + 1 < len(a) - 1 or 2 * i + 2 < len(a) - 1:
                self.assertEqual(arr[i] > arr[2 * i + 1], True, 'form are incorrect')
                self.assertEqual(arr[i] > arr[2 * i + 2], True, 'form are incorrect')

    def test_more_arr(self):
        heap = Heap.Heap()
        a = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],[6, 5, 2, 1, 3, 8, 11, 4, 9, 7],[7, 5],[5, 7, 8, 4, 10]]
        for i in a:
            arr = heap.MakeHeap(i, 3)
            count = 0
            for j in arr:
                if j != None:
                 count +=1
            self.assertEqual(len(i) == count, True, 'digits are incorrect')
            self.assertEqual(len(arr) == 15, True, 'None are incorrect')
            self.assertEqual(arr[0] == max(i), True, 'first elem == max element are incorrect')
#,[6, 5, 2, 1, 3, 8, 11, 4, 9, 7], [11, 5], [5, 7, 8, 4, 10]
    def test_max_arr(self):
        heap = Heap.Heap()
        a = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],[6, 5, 2, 1, 3, 8, 11, 4, 9, 7],[11, 5],[5, 7, 8, 4, 10]]
        for j in a:
            arr = heap.MakeHeap(j, 3)
            arr_res = []
            for i in arr:
                if i != None:
                    arr_res.append(i)
            print(arr_res)
            del arr_res[0]
            arr_max = heap.GetMax()
            print(arr_max, max(arr_res))
            self.assertEqual(arr_max == max(arr_res) , True, 'first element are incorrect')

if __name__ == '__main__':
    unittest.main()
