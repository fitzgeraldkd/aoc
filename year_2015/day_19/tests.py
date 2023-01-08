import unittest
from unittest.mock import patch

from utils.setup import read_inputs
from year_2015.day_19.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 576)

    def test_part_2(self):
        self.assertEqual(part_2(), 207)


class TestExamples(unittest.TestCase):

    get_input = lambda _, molecule: [*read_inputs(__file__, 'sample.txt'), '\n', molecule]

    def test_part_1(self):

        with patch('year_2015.day_19.solution.read_inputs', return_value=self.get_input('HOH')):
            self.assertEqual(part_1(), 4)
        with patch('year_2015.day_19.solution.read_inputs', return_value=self.get_input('HOHOHO')):
            self.assertEqual(part_1(), 7)

    def test_part_2(self):

        with patch('year_2015.day_19.solution.read_inputs', return_value=self.get_input('HOH')):
            self.assertEqual(part_2(), 3)
        with patch('year_2015.day_19.solution.read_inputs', return_value=self.get_input('HOHOHO')):
            self.assertEqual(part_2(), 6)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
