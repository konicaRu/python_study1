import unittest
import BinarySearch


class MyTestCase(unittest.TestCase):
    def test_list_exept(self):
        arr = arr = [i for i in range(1, 99)]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 49
        self.assertEqual(bi.GetResult() == 1, True)
        arr = [3]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 17
        self.assertEqual(bi.GetResult() == -1, True)
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 3
        self.assertEqual(bi.GetResult() == 1, True)
        BinarySearch.N = 21
        self.assertEqual(bi.GetResult() == -1, True)
        arr = []
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 17
        self.assertEqual(bi.GetResult() == -1, True)
        arr = [3, 4]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 17
        self.assertEqual(bi.GetResult() == -1, True)
        arr = [3, 4]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 3
        self.assertEqual(bi.GetResult() == 1, True)
        arr = [3, 4]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 4
        self.assertEqual(bi.GetResult() == 1, True)
        arr = [3, 4]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 5
        self.assertEqual(bi.GetResult() == 1, False)

    def test_list_10Right(self):
        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 1
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 11
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 3
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 4
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 5
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 6
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 7
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 8
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 9
        self.assertEqual(bi.GetResult() == 1, False)

        arr = [1, 3, 4, 5, 6, 7, 8, 10, 11]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 10
        self.assertEqual(bi.GetResult() == 1, True)

    def test_list_10Wrong(self):
        arr = [3, 11, 17, 20, 31, 33, 38, 38, 39, 42, 43, 44, 44, 46, 50]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 17
        self.assertEqual(bi.GetResult() == 1, True)

        arr = [3, 11, 17, 20, 31, 33, 38, 38, 39, 42, 43, 44, 44, 46, 50]
        bi = BinarySearch.BinarySearch(arr)
        BinarySearch.N = 3
        self.assertEqual(bi.GetResult() == -1, False)

        BinarySearch.N = 21
        self.assertEqual(bi.GetResult() == -1, True)


if __name__ == '__main__':
    unittest.main()
