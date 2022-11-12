import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_03.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 2081)

    def test_part_2(self):
        self.assertEqual(part_2(), 2341)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1('>'), 2)
        self.assertEqual(part_1('^>v<'), 4)
        self.assertEqual(part_1('^v^v^v^v^v'), 2)

    def test_part_2(self):
        self.assertEqual(part_2('^v'), 3)
        self.assertEqual(part_2('^>v<'), 3)
        self.assertEqual(part_2('^v^v^v^v^v'), 11)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
