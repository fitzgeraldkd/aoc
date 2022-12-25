import os
import sys
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_25.solution import decimal_to_snafu, part_1, part_2, snafu_to_decimal
from utils.setup import read_inputs


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), '2-0==21--=0==2201==2')

    def test_part_2(self):
        self.assertEqual(part_2(), None)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('day_25.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')):
            self.assertEqual(part_1(), '2=-1=0')


class TestUtils(unittest.TestCase):

    DECIMAL_SNAFU_PAIRS = [
        (1, '1'),
        (2, '2'),
        (3, '1='),
        (4, '1-'),
        (5, '10'),
        (6, '11'),
        (7, '12'),
        (8, '2='),
        (9, '2-'),
        (10, '20'),
        (15, '1=0'),
        (20, '1-0'),
        (2022, '1=11-2'),
        (12345, '1-0---0'),
        (314159265, '1121-1110-1=0')
    ]

    def test_decimal_to_snafu(self):
        for decimal, snafu in self.DECIMAL_SNAFU_PAIRS:
            self.assertEqual(decimal_to_snafu(decimal), snafu, f'Input: {decimal}')

    def test_snafu_to_decimal(self):
        for decimal, snafu in self.DECIMAL_SNAFU_PAIRS:
            self.assertEqual(snafu_to_decimal(snafu), decimal, f'Input: {snafu}')


if __name__ == '__main__':
    unittest.main()
