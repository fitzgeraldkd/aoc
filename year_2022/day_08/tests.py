import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2022.day_08.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 1801)

    def test_part_2(self):
        self.assertEqual(part_2(), 209880)


class TestExamples(unittest.TestCase):

    SAMPLE_FOREST = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390'
    ]

    def test_part_1(self):
        with patch('year_2022.day_08.solution.read_inputs', return_value=self.SAMPLE_FOREST):
            self.assertEqual(part_1(), 21)

    def test_part_2(self):
        with patch('year_2022.day_08.solution.read_inputs', return_value=self.SAMPLE_FOREST):
            self.assertEqual(part_2(), 8)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
