import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_02.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 1588178)

    def test_part_2(self):
        self.assertEqual(part_2(), 3783758)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1([[2, 3, 4]]), 58)
        self.assertEqual(part_1([[1, 1, 10]]), 43)
        self.assertEqual(part_1([[2, 3, 4], [1, 1, 10]]), 101)

    def test_part_2(self):
        self.assertEqual(part_2([[2, 3, 4]]), 34)
        self.assertEqual(part_2([[1, 1, 10]]), 14)
        self.assertEqual(part_2([[2, 3, 4], [1, 1, 10]]), 48)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
