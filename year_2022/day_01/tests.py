import unittest
import os
import sys
from unittest import mock
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2022.day_01.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 74394)

    def test_part_2(self):
        self.assertEqual(part_2(), 212836)


class TestExamples(unittest.TestCase):

    EXAMPLE_DATA = [
        '1000',
        '2000',
        '3000',
        '',
        '4000',
        '',
        '5000',
        '6000',
        '',
        '7000',
        '8000',
        '9000',
        '',
        '10000'
    ]

    @mock.patch('year_2022.day_01.solution.read_inputs', return_value=EXAMPLE_DATA)
    def test_part_1(self, mocked_read_inputs):
        self.assertEqual(part_1(), 24000)

    @mock.patch('year_2022.day_01.solution.read_inputs', return_value=EXAMPLE_DATA)
    def test_part_2(self, mocked_read_inputs):
        self.assertEqual(part_2(), 45000)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
