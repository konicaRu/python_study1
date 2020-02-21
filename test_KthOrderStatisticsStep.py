import unittest
import KthOrderStatisticsStep


class MyTestCase(unittest.TestCase):
    def test_five(self):
        a = [5, 4, 1, 2, 3]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 4, 0)) == [0,2] , True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 4, 4)) == [2, 4], True)
    def test_six(self):
        a = [5, 4, 1, 2, 3, 6]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 0)) == [0, 5] , True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 4)) == [0, 5], True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 5, 5)) == [5], True)
    def test_seven(self):
        a = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 6, 0)) == [0, 2] , True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 6, 4)) == [2, 6], True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 6, 2)) == [2], True)
    def test_twentySix(self):
        a = [17, 4, 16, 3, 5, 11, 18, 26, 27, 19, 22, 13, 1, 20, 23, 7, 8, 15, 9, 6, 10, 24, 12, 14, 2, 21, 25]
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 26, 0)) == [0, 7] , True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 26, 20)) == [7, 26], True)
        self.assertEqual((KthOrderStatisticsStep.KthOrderStatisticsStep(a, 0, 26, 7)) == [7], True)


if __name__ == '__main__':
    unittest.main()
