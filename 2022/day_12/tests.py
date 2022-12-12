import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_12.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 339)

    def test_part_2(self):
        self.assertEqual(part_2(), 332)


class TestExamples(unittest.TestCase):

    SAMPLE_MAP = [
        'Sabqponm',
        'abcryxxl',
        'accszExk',
        'acctuvwj',
        'abdefghi'
    ]

    def test_part_1(self):
        with patch('day_12.solution.read_inputs', return_value=self.SAMPLE_MAP):
            self.assertEqual(part_1(), 31)

    def test_part_2(self):
        with patch('day_12.solution.read_inputs', return_value=self.SAMPLE_MAP):
            self.assertEqual(part_2(), 29)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
