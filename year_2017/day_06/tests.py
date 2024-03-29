import unittest
from unittest.mock import patch

from year_2017.day_06.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 11137)

    def test_part_2(self):
        self.assertEqual(part_2(), 1037)


class TestExamples(unittest.TestCase):

    SAMPLE_BANKS = ['0  2  7  0']

    def test_part_1(self):
        with patch('year_2017.day_06.solution.read_inputs', return_value=self.SAMPLE_BANKS):
            self.assertEqual(part_1(), 5)

    def test_part_2(self):
        with patch('year_2017.day_06.solution.read_inputs', return_value=self.SAMPLE_BANKS):
            self.assertEqual(part_2(), 4)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
