import unittest
from unittest.mock import patch

from utils.setup import read_inputs
from year_2015.day_17.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 4372)

    def test_part_2(self):
        self.assertEqual(part_2(), 4)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('year_2015.day_17.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')),\
                patch('year_2015.day_17.solution.TARGET_VOLUME', 25):
            self.assertEqual(part_1(), 4)

    def test_part_2(self):
        with patch('year_2015.day_17.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')),\
                patch('year_2015.day_17.solution.TARGET_VOLUME', 25):
            self.assertEqual(part_2(), 3)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
