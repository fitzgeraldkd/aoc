import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_15.solution import part_1, part_2
from utils.setup import read_inputs

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 5461729)

    @unittest.skip
    # Takes about two minutes to run.
    def test_part_2(self):
        self.assertEqual(part_2(), 10621647166538)


class TestExamples(unittest.TestCase):

    @patch('day_15.solution.read_inputs', return_value=read_inputs(CURRENT_DIRECTORY, 'sample.txt'))
    @patch('day_15.solution.PART_1_TARGET_ROW', 10)
    def test_part_1(self, mocked_read_inputs):
        self.assertEqual(part_1(), 26)

    @patch('day_15.solution.read_inputs', return_value=read_inputs(CURRENT_DIRECTORY, 'sample.txt'))
    @patch('day_15.solution.PART_2_MAX_COORDINATE', 20)
    def test_part_2(self, mocked_read_inputs):
        self.assertEqual(part_2(), 56000011)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
