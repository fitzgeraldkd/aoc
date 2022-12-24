import unittest
from unittest import mock

from year_2017.day_16.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'fnloekigdmpajchb')

    def test_part_2(self):
        self.assertEqual(part_2(), 'amkjepdhifolgncb')


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        commands = ['s1', 'x3/4', 'pe/b']
        with mock.patch('year_2017.day_16.solution.STARTING_LINE', 'abcde'):
            self.assertEqual(part_1(commands), 'baedc')


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
