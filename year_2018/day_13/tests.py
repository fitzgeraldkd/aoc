import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_13.solution import part_1, part_2
from utils.setup import read_inputs

CURRENT_DIRECTORY = os.path.realpath(__file__)


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), '118,66')

    def test_part_2(self):
        self.assertEqual(part_2(), '70,129')


class TestExamples(unittest.TestCase):

    @patch('year_2018.day_13.solution.read_inputs', return_value=read_inputs(CURRENT_DIRECTORY, 'sample.txt'))
    def test_part_1(self, mocked_read_inputs):
        self.assertEqual(part_1(), '7,3')

    @patch('year_2018.day_13.solution.read_inputs', return_value=read_inputs(CURRENT_DIRECTORY, 'sample2.txt'))
    def test_part_2(self, mocked_read_inputs):
        self.assertEqual(part_2(), '6,4')


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
