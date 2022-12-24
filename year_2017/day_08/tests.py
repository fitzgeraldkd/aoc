import unittest
from unittest.mock import patch

from year_2017.day_08.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 5946)

    def test_part_2(self):
        self.assertEqual(part_2(), 6026)


class TestExamples(unittest.TestCase):

    example_input = [
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10'
    ]

    def test_part_1(self):
        with patch('year_2017.day_08.solution.read_inputs', return_value=self.example_input):
            self.assertEqual(part_1(), 1)

    def test_part_2(self):
        with patch('year_2017.day_08.solution.read_inputs', return_value=self.example_input):
            self.assertEqual(part_2(), 10)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
