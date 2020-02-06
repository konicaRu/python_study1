import unittest
import SelectionSortStep


class MyTestCase(unittest.TestCase):
    def test_fife(self):
        arr = [4,3,1,2,5]
        b = 0
        self.assertEqual(SelectionSortStep.SelectionSortStep(arr, b) == sorted(arr), True)
        arr = [1, 4, 3,  2, 5]
        b = 0
        self.assertEqual(SelectionSortStep.SelectionSortStep(arr, b) == sorted(arr), True)
        arr = [4, 3, 1, 2, 5]
        b = 1
        self.assertEqual(SelectionSortStep.SelectionSortStep(arr, b) == [4,1,2,3,5], True)
        arr = [4, 3, 2, 1, 5]
        b = 2
        self.assertEqual(SelectionSortStep.SelectionSortStep(arr, b) == [4,3,1,2,5], True)
        arr = [4, 3, 2, 5, 1]
        b = 3
        self.assertEqual(SelectionSortStep.SelectionSortStep(arr, b) == [4, 3, 2, 1, 5], True)
        arr = [4, 3, 2, 5, 1]
        b = 4
        self.assertEqual(SelectionSortStep.SelectionSortStep(arr, b) == [4, 3, 2, 5, 1], True)


if __name__ == '__main__':
    unittest.main()
