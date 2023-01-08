import unittest
from unittest.mock import patch

from utils.setup import read_inputs
from year_2015.day_14.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 2640)

    def test_part_2(self):
        self.assertEqual(part_2(), 1102)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('year_2015.day_14.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')),\
                patch('year_2015.day_14.solution.RACE_DURATION', 1000):
            self.assertEqual(part_1(), 1120)

    def test_part_2(self):
        with patch('year_2015.day_14.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')),\
                patch('year_2015.day_14.solution.RACE_DURATION', 1000):
            self.assertEqual(part_2(), 689)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
