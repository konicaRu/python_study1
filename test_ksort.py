import unittest
import ksort


class MyTestCase(unittest.TestCase):
    def test_correct_values(self):
        count = 0
        k = ksort.ksort()
        correct_values = ['a01', 'a02', 'a03', 'b33', 'c78', 'e45', 'f56', 'g89', 'h22']
        for i in correct_values:
            if k.add(i) == True:
                count += 1
        self.assertEqual(count == 9, True)

    def test_uncorrect_values(self):
        count = 0
        k = ksort.ksort()
        uncorrect_values = ['a0154', 'aa02', 'z0a', 'a456', 'as98a','a', 'aa','123', 'g4']
        for i in uncorrect_values:
            if k.add(i) == False:
                count += 1
        self.assertEqual(count == 9, True)

if __name__ == '__main__':
    unittest.main()
