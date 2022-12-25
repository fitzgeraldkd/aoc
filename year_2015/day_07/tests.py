import unittest
from unittest.mock import patch

from utils.setup import read_inputs
from year_2015.day_07.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 3176)

    def test_part_2(self):
        self.assertEqual(part_2(), 14710)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('year_2015.day_07.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')):
            with patch('year_2015.day_07.solution.TARGET_WIRE', 'd'):
                self.assertEqual(part_1(), 72)
            with patch('year_2015.day_07.solution.TARGET_WIRE', 'e'):
                self.assertEqual(part_1(), 507)
            with patch('year_2015.day_07.solution.TARGET_WIRE', 'f'):
                self.assertEqual(part_1(), 492)
            with patch('year_2015.day_07.solution.TARGET_WIRE', 'g'):
                self.assertEqual(part_1(), 114)
            with patch('year_2015.day_07.solution.TARGET_WIRE', 'h'):
                self.assertEqual(part_1(), 65412)
            with patch('year_2015.day_07.solution.TARGET_WIRE', 'i'):
                self.assertEqual(part_1(), 65079)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
