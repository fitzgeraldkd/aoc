import unittest
from unittest.mock import patch

from utils.setup import read_inputs
from year_2015.day_25.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 2650453)

    def test_part_2(self):
        self.assertEqual(part_2(), None)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('year_2015.day_25.solution.read_inputs', return_value=['2 1']):
            self.assertEqual(part_1(), 31916031)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
