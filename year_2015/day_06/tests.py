import unittest
from unittest.mock import patch

from year_2015.day_06.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 569999)

    def test_part_2(self):
        self.assertEqual(part_2(), 17836115)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        sample_instructions = [
            'turn on 0,0 through 999,999',
            'toggle 0,0 through 999,0',
            'turn off 499,499 through 500,500'
        ]
        with patch('year_2015.day_06.solution.read_inputs', return_value=sample_instructions):
            self.assertEqual(part_1(), 998996)

    def test_part_2(self):
        sample_instructions = [
            'turn on 0,0 through 0,0',
            'toggle 0,0 through 999,999'
        ]
        with patch('year_2015.day_06.solution.read_inputs', return_value=sample_instructions):
            self.assertEqual(part_2(), 2000001)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
