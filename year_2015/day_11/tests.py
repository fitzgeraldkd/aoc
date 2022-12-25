import unittest
from unittest.mock import patch

from year_2015.day_11.solution import part_1, part_2, passes_rules


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'cqjxxyzz')

    def test_part_2(self):
        self.assertEqual(part_2(), 'cqkaabcc')


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('year_2015.day_11.solution.read_inputs', return_value=['abcdefgh']):
            self.assertEqual(part_1(), 'abcdffaa')
        with patch('year_2015.day_11.solution.read_inputs', return_value=['ghijklmn']):
            # TODO: Fix this assertion.
            self.assertEqual(part_2(), 'ghjaabcc')


class TestUtils(unittest.TestCase):

    def test_passes_rules(self):
        self.assertFalse(passes_rules('hijklmmn'))
        self.assertFalse(passes_rules('abbceffg'))
        self.assertFalse(passes_rules('abbcegjk'))
        self.assertTrue(passes_rules('abcdffaa'))
        self.assertTrue(passes_rules('ghjaabcc'))


if __name__ == '__main__':
    unittest.main()
