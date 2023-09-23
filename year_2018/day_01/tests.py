import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_01.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 442)

    def test_part_2(self):
        self.assertEqual(part_2(), 59908)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1([1, -2, 3, 1]), 3)
        self.assertEqual(part_1([1, 1, 1]), 3)
        self.assertEqual(part_1([1, 1, -2]), 0)
        self.assertEqual(part_1([-1, -2, -3]), -6)

    def test_part_2(self):
        self.assertEqual(part_2([1, -2, 3, 1]), 2)
        self.assertEqual(part_2([1, -1]), 0)
        self.assertEqual(part_2([3, 3, 4, -2, -4]), 10)
        self.assertEqual(part_2([-6, 3, 8, 5, -6]), 5)
        self.assertEqual(part_2([7, 7, -2, -7, -4]), 14)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
