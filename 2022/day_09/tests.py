import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_09.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 6212)

    def test_part_2(self):
        self.assertEqual(part_2(), 2522)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        sample_instructions = [
            'R 4',
            'U 4',
            'L 3',
            'D 1',
            'R 4',
            'D 1',
            'L 5',
            'R 2'
        ]
        with patch('day_09.solution.read_inputs', return_value=sample_instructions):
            self.assertEqual(part_1(), 13)

    def test_part_2(self):
        sample_instructions = [
            'R 5',
            'U 8',
            'L 8',
            'D 3',
            'R 17',
            'D 10',
            'L 25',
            'U 20'
        ]
        with patch('day_09.solution.read_inputs', return_value=sample_instructions):
            self.assertEqual(part_2(), 36)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
