import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_09.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 418237)

    def test_part_2(self):
        self.assertEqual(part_2(), 3505711612)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1([9, 25]), 32)
        self.assertEqual(part_1([10, 1618]), 8317)
        self.assertEqual(part_1([13, 7999]), 146373)
        self.assertEqual(part_1([17, 1104]), 2764)
        self.assertEqual(part_1([21, 6111]), 54718)
        self.assertEqual(part_1([30, 5807]), 37305)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
