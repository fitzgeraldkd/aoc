import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_13.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 5185)

    def test_part_2(self):
        self.assertEqual(part_2(), 23751)


class TestExamples(unittest.TestCase):

    SAMPLE_PAIRS = [
        '[1,1,3,1,1]',
        '[1,1,5,1,1]',
        '\n',
        '[[1],[2,3,4]]',
        '[[1],4]',
        '\n',
        '[9]',
        '[[8,7,6]]',
        '\n',
        '[[4,4],4,4]',
        '[[4,4],4,4,4]',
        '\n',
        '[7,7,7,7]',
        '[7,7,7]',
        '\n',
        '[]',
        '[3]',
        '\n',
        '[[[]]]',
        '[[]]',
        '\n',
        '[1,[2,[3,[4,[5,6,7]]]],8,9]',
        '[1,[2,[3,[4,[5,6,0]]]],8,9]'
    ]

    def test_part_1(self):
        with patch('day_13.solution.read_inputs', return_value=self.SAMPLE_PAIRS):
            self.assertEqual(part_1(), 13)

    def test_part_2(self):
        with patch('day_13.solution.read_inputs', return_value=self.SAMPLE_PAIRS):
            self.assertEqual(part_2(), 140)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
