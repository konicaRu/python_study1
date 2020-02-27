import unittest
import HeapSort


class MyTestCase(unittest.TestCase):
    def test_arr_ten(self):
        heap = HeapSort.HeapSort()
        a = [1, 1, 1, 2, 3, 4, 5, 6, 7]
        heap.HeapSort(a)
        self.assertEqual(heap.HeapObject == [7, 6, 4, 5, 1, 1, 3, 1, 2], True)
        self.assertEqual(heap.GetNextMax() == 7, True)

        a = [6, 5, 2, 1, 3, 8, 11, 4, 9, 7]
        heap.HeapSort(a)
        self.assertEqual(heap.HeapObject == [11, 9, 8, 5, 7, 2, 6, 1, 4, 3], True)
        a = [6]
        heap.HeapSort(a)
        self.assertEqual(heap.HeapObject == [6], True)
        a = [6, 5]
        heap.HeapSort(a)
        self.assertEqual(heap.HeapObject == [6, 5], True)
        a = [110, 9, 40, 70, 80, 30, 10, 20, 50, 60, 65, 31, 29, 11, 90]
        heap.HeapSort(a)
        self.assertEqual(heap.HeapObject == [110, 80, 90, 50, 70, 31, 40, 9, 20, 60, 65, 30, 29, 10, 11], True)
        a = []
        heap.HeapSort(a)
        self.assertEqual(heap.HeapObject == [], True)
        self.assertEqual(heap.GetNextMax() == -1, True)

        a = [1, 1, 1, 2, 3, 4, 5, 6, 7]
        heap.HeapSort(a)
        self.assertEqual(heap.HeapObject == [7, 6, 4, 5, 1, 1, 3, 1, 2], True)
        self.assertEqual(heap.GetNextMax() == 7, True)

    def test_arr_del(self):
        heap = HeapSort.HeapSort()
        a = [2, 5, 6]
        heap.HeapSort(a)
        self.assertEqual(heap.GetNextMax() == 6, True)
        self.assertEqual(heap.HeapObject == [5, 2, None], True)
        self.assertEqual(heap.GetNextMax() == 5, True)
        self.assertEqual(heap.HeapObject == [2, None, None], True)
        self.assertEqual(heap.GetNextMax() == 2, True)
        self.assertEqual(heap.HeapObject == [None, None, None], True)
        self.assertEqual(heap.GetNextMax() == -1, True)


if __name__ == '__main__':
    unittest.main()
