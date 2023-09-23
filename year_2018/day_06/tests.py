import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_06.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 4771)

    def test_part_2(self):
        self.assertEqual(part_2(), 39149)


class TestExamples(unittest.TestCase):

    SAMPLE_COORDINATES = [
        '1, 1',
        '1, 6',
        '8, 3',
        '3, 4',
        '5, 5',
        '8, 9'
    ]

    def test_part_1(self):
        with patch('year_2018.day_06.solution.read_inputs', return_value=self.SAMPLE_COORDINATES):
            self.assertEqual(part_1(), 17)

    def test_part_2(self):
        with patch('year_2018.day_06.solution.read_inputs', return_value=self.SAMPLE_COORDINATES), \
                patch('year_2018.day_06.solution.PART_2_TARGET_DISTANCE', 32):
            self.assertEqual(part_2(), 16)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
