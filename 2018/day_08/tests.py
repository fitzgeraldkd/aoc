import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_08.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 49180)

    def test_part_2(self):
        self.assertEqual(part_2(), 20611)


class TestExamples(unittest.TestCase):

    SAMPLE_NODES = ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2']

    def test_part_1(self):
        with patch('day_08.solution.read_inputs', return_value=self.SAMPLE_NODES):
            self.assertEqual(part_1(), 138)

    def test_part_2(self):
        with patch('day_08.solution.read_inputs', return_value=self.SAMPLE_NODES):
            self.assertEqual(part_2(), 66)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
