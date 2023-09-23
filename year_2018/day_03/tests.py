import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_03.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 98005)

    def test_part_2(self):
        self.assertEqual(part_2(), 331)


class TestExamples(unittest.TestCase):

    SAMPLE_CLAIMS = [
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2'
        ]

    def test_part_1(self):
        with patch('year_2018.day_03.solution.read_inputs', return_value=self.SAMPLE_CLAIMS):
            self.assertEqual(part_1(), 4)

    def test_part_2(self):
        with patch('year_2018.day_03.solution.read_inputs', return_value=self.SAMPLE_CLAIMS):
            self.assertEqual(part_2(), 3)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
