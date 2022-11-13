import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_13.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 1476)

    def test_part_2(self):
        self.assertEqual(part_2(), 3937334)


class TestExamples(unittest.TestCase):

    firewall = [
        (0, 3),
        (1, 2),
        (4, 4),
        (6, 4)
    ]

    def test_part_1(self):
        self.assertEqual(part_1(self.firewall), 24)

    def test_part_2(self):
        self.assertEqual(part_2(self.firewall), 10)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
