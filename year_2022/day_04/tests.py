import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2022.day_04.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 524)

    def test_part_2(self):
        self.assertEqual(part_2(), 798)


class TestExamples(unittest.TestCase):

    SAMPLE_PAIRS = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8'
    ]

    def test_part_1(self):
        with patch('year_2022.day_04.solution.read_inputs', return_value=self.SAMPLE_PAIRS):
            self.assertEqual(part_1(), 2)

    def test_part_2(self):
        with patch('year_2022.day_04.solution.read_inputs', return_value=self.SAMPLE_PAIRS):
            self.assertEqual(part_2(), 4)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
