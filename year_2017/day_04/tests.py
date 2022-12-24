import unittest
from unittest.mock import patch

from year_2017.day_04.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 466)

    def test_part_2(self):
        self.assertEqual(part_2(), 251)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        sample_passphrases = [
            'aa bb cc dd ee',
            'aa bb cc dd aa',
            'aa bb cc dd aaa'
        ]

        with patch('year_2017.day_04.solution.read_inputs', return_value=sample_passphrases):
            self.assertEqual(part_1(), 2)

    def test_part_2(self):
        sample_passphrases = [
            'abcde fghij',
            'abcde xyz ecdab',
            'a ab abc abd abf abj',
            'iiii oiii ooii oooi oooo',
            'oiii ioii iioi iiio'
        ]

        with patch('year_2017.day_04.solution.read_inputs', return_value=sample_passphrases):
            self.assertEqual(part_2(), 3)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
