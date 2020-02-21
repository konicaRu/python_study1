import unittest
import KthOrderStatisticsStep


class MyTestCase(unittest.TestCase):
    def test_fore(self):
        a = [5, 4, 1, 2]
        example1 = KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 3, 0)
        self.assertEqual(example1 == ([0, 1], [1, 2, 4, 5]), True)
        example2 = KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 3, 3)
        self.assertEqual(example2 == ([1, 3], [1, 2, 4, 5]), True)

    def test_five(self):
        a = [5, 4, 1, 2, 3]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 4, 0)) == ([0, 2], [1, 2, 3, 4, 5]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 4, 4)) == ([2, 4], [1, 2, 3, 4, 5]), True)

    def test_six(self):
        a = [5, 4, 1, 2, 3, 6]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 0)) == ([0, 5], [1, 2, 3, 4, 5, 6]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 4)) == ([0, 5], [1, 2, 3, 4, 5, 6]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 5)) == ([5], [1, 2, 3, 4, 5, 6]), True)

    def test_seven(self):
        a = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 6, 0)) == ([0, 2], [1, 4, 5, 6, 7, 2, 3]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 6, 4)) == ([2, 6], [1, 4, 5, 6, 7, 2, 3]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 6, 2)) == ([2], [1, 4, 5, 6, 7, 2, 3]), True)

    def test_seven2(self):
        a = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 0)) == ([0, 2], [1, 4, 5, 6, 7, 2, 3]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 4)) == ([2, 5], [1, 4, 5, 6, 7, 2, 3]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 2)) == ([2], [1, 4, 5, 6, 7, 2, 3]), True)

    def test_EITH(self):
        a = [5, 6, 7, 4, 1, 8, 11, 10]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 7, 0)) == ([0, 6], [1, 4, 5, 6, 7, 8, 10, 11]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 7, 7)) == ([6, 7], [1, 4, 5, 6, 7, 8, 10, 11]), True)
        

    def test_twentySix(self):
        a = [17, 4, 16, 3, 5, 11, 18, 26, 27, 19, 22, 13, 1, 20, 23, 7, 8, 15, 9, 6, 10, 24, 12, 14, 2, 21, 25]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 26, 0)) == ([0, 7], [3, 4, 5, 16, 17, 11, 18, 19, 26, 27, 1, 13, 20, 22, 23, 6, 7, 8, 9, 15, 2, 10, 12, 14, 24, 21, 25]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 26, 20)) == ([7, 26], [3, 4, 5, 16, 17, 11, 18, 19, 26, 27, 1, 13, 20, 22, 23, 6, 7, 8, 9, 15, 2, 10, 12, 14, 24, 21, 25]), True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 26, 7)) == ([7], [3, 4, 5, 16, 17, 11, 18, 19, 26, 27, 1, 13, 20, 22, 23, 6, 7, 8, 9, 15, 2, 10, 12, 14, 24, 21, 25]), True)


if __name__ == '__main__':
    unittest.main()
