import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_02.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 14531)

    def test_part_2(self):
        self.assertEqual(part_2(), 11258)


class TestExamples(unittest.TestCase):

    SAMPLE_INSTRUCTIONS = [
        ['A', 'Y'],
        ['B', 'X'],
        ['C', 'Z']
    ]

    def test_part_1(self):
        self.assertEqual(part_1(self.SAMPLE_INSTRUCTIONS), 15)

    def test_part_2(self):
        self.assertEqual(part_2(self.SAMPLE_INSTRUCTIONS), 12)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
