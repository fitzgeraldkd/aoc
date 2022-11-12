import unittest
import os
import sys
from unittest import mock
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_12.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 378)

    def test_part_2(self):
        self.assertEqual(part_2(), 204)


class TestExamples(unittest.TestCase):

    example_input = [
        '0 <-> 2',
        '1 <-> 1',
        '2 <-> 0, 3, 4',
        '3 <-> 2, 4',
        '4 <-> 2, 3, 6',
        '5 <-> 6',
        '6 <-> 4, 5',
    ]

    def test_part_1(self):
        with mock.patch('day_12.solution.read_inputs', return_value=self.example_input):
            self.assertEqual(part_1(), 6)

    def test_part_1(self):
        with mock.patch('day_12.solution.read_inputs', return_value=self.example_input):
            self.assertEqual(part_2(), 2)

class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
