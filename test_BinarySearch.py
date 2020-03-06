import unittest
import BinarySearch


class MyTestCase(unittest.TestCase):
    def test_100Minus49(self):
        arr = [i for i in range(1, 100) if i != 49]
        bi = BinarySearch.BinarySearch(arr)
        bi.Step(49)
        self.assertEqual(bi.Left == 0, True)
        self.assertEqual(bi.Right == 47, True)
        self.assertEqual(bi.pivot == 48, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 24, True)
        self.assertEqual(bi.Right == 47, True)
        self.assertEqual(bi.pivot == 23, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 36, True)
        self.assertEqual(bi.Right == 47, True)
        self.assertEqual(bi.pivot == 35, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 42, True)
        self.assertEqual(bi.Right == 47, True)
        self.assertEqual(bi.pivot == 41, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 45, True)
        self.assertEqual(bi.Right == 47, True)
        self.assertEqual(bi.pivot == 44, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 47, True)
        self.assertEqual(bi.Right == 47, True)
        self.assertEqual(bi.pivot == 46, True)
        self.assertEqual(bi.GetResult() == -1, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 48, True)
        self.assertEqual(bi.Right == 47, True)
        self.assertEqual(bi.pivot == 47, True)
        self.assertEqual(bi.GetResult() == -1, True)

    def test_100Plus49(self):
        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        bi.Step(49)
        self.assertEqual(bi.Left == 0, True)
        self.assertEqual(bi.Right == 48, True)
        self.assertEqual(bi.pivot == 49, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 25, True)
        self.assertEqual(bi.Right == 48, True)
        self.assertEqual(bi.pivot == 24, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 37, True)
        self.assertEqual(bi.Right == 48, True)
        self.assertEqual(bi.pivot == 36, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 43, True)
        self.assertEqual(bi.Right == 48, True)
        self.assertEqual(bi.pivot == 42, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 46, True)
        self.assertEqual(bi.Right == 48, True)
        self.assertEqual(bi.pivot == 45, True)
        self.assertEqual(bi.GetResult() == 0, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 48, True)
        self.assertEqual(bi.Right == 48, True)
        self.assertEqual(bi.pivot == 47, True)
        self.assertEqual(bi.GetResult() == 1, True)

        bi.Step(49)
        self.assertEqual(bi.Left == 48, True)
        self.assertEqual(bi.Right == 48, True)
        self.assertEqual(bi.pivot == 48, True)
        self.assertEqual(bi.GetResult() == 1, True)


    def test_list_100(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,  50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
               89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(49)
        self.assertEqual(bi.GetResult() == -1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(15)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(1)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(99)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(25)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(24)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(23)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(75)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(7):
            bi.Step(77)
        self.assertEqual(bi.GetResult() == 1, True)

    def test_zero(self):
        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(2):
            bi.Step(77)
        self.assertEqual(bi.GetResult() == 0, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(1):
            bi.Step(49)
        self.assertEqual(bi.GetResult() == 0, True)

        arr = [i for i in range(1, 100)]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(5):
            bi.Step(49)
        self.assertEqual(bi.GetResult() == 0, True)

    def test_list_10(self):
        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(3):
            bi.Step(1)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(3):
            bi.Step(2)
        self.assertEqual(bi.GetResult() == -1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(3):
            bi.Step(4)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(4):
            bi.Step(5)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(4):
            bi.Step(6)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(4):
            bi.Step(5)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(3):
            bi.Step(7)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(4):
            bi.Step(8)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(4):
            bi.Step(9)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(4):
            bi.Step(10)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range (3):
            bi.Step(3)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(3):
            bi.Step(9)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(3):
            bi.Step(6)
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        for i in range(3):
            bi.Step(7)
        self.assertEqual(bi.GetResult() == 1, True)

if __name__ == '__main__':
    unittest.main()
