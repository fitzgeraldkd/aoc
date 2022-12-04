import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_05.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 374269)

    def test_part_2(self):
        self.assertEqual(part_2(), 27720699)


class TestExamples(unittest.TestCase):

    SAMPLE_OFFSETS = ['0', '3', '0', '1', '-3']

    def test_part_1(self):
        with patch('day_05.solution.read_inputs', return_value=self.SAMPLE_OFFSETS):
            self.assertEqual(part_1(), 5)

    def test_part_2(self):
        with patch('day_05.solution.read_inputs', return_value=self.SAMPLE_OFFSETS):
            self.assertEqual(part_2(), 10)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
