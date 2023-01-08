import unittest
from unittest.mock import patch

from year_2015.day_20.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 776160)

    def test_part_2(self):
        self.assertEqual(part_2(), 786240)


class TestExamples(unittest.TestCase):

    def test_part_1(self):

        with patch('year_2015.day_20.solution.read_inputs', return_value=['10']):
            self.assertEqual(part_1(), 1)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['30']):
            self.assertEqual(part_1(), 2)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['40']):
            self.assertEqual(part_1(), 3)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['60']):
            self.assertEqual(part_1(), 4)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['70']):
            self.assertEqual(part_1(), 4)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['80']):
            self.assertEqual(part_1(), 6)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['120']):
            self.assertEqual(part_1(), 6)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['130']):
            self.assertEqual(part_1(), 8)
        with patch('year_2015.day_20.solution.read_inputs', return_value=['150']):
            self.assertEqual(part_1(), 8)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
