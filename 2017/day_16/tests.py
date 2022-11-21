import unittest
import os
import sys
from unittest import mock
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_16.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'fnloekigdmpajchb')

    def test_part_2(self):
        self.assertEqual(part_2(), 'amkjepdhifolgncb')
        # aehmpjfcnilbogkd
        # fdloikegnmpajchb


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        commands = ['s1', 'x3/4', 'pe/b']
        with mock.patch('day_16.solution.STARTING_LINE', 'abcde'):
            self.assertEqual(part_1(commands), 'baedc')


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
