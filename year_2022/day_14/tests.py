import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2022.day_14.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 728)

    def test_part_2(self):
        self.assertEqual(part_2(), 27623)


class TestExamples(unittest.TestCase):

    SAMPLE_ROCKS = [
        '498,4 -> 498,6 -> 496,6',
        '503,4 -> 502,4 -> 502,9 -> 494,9'
    ]

    def test_part_1(self):
        with patch('year_2022.day_14.solution.read_inputs', return_value=self.SAMPLE_ROCKS):
            self.assertEqual(part_1(), 24)

    def test_part_2(self):
        with patch('year_2022.day_14.solution.read_inputs', return_value=self.SAMPLE_ROCKS):
            self.assertEqual(part_2(), 93)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
