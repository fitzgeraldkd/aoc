import unittest
from unittest.mock import patch

from year_2017.day_18.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 9423)

    def test_part_2(self):
        self.assertEqual(part_2(), 7620)


class TestExamples(unittest.TestCase):


    def test_part_1(self):

        instructions = [
            'set a 1',
            'add a 2',
            'mul a a',
            'mod a 5',
            'snd a',
            'set a 0',
            'rcv a',
            'jgz a -1',
            'set a 1',
            'jgz a -2'
        ]

        with patch('year_2017.day_18.solution.read_inputs', return_value=instructions):
            self.assertEqual(part_1(), 4)

    def test_part_2(self):

        instructions = [
            'snd 1',
            'snd 2',
            'snd p',
            'rcv a',
            'rcv b',
            'rcv c',
            'rcv d'
        ]

        with patch('year_2017.day_18.solution.read_inputs', return_value=instructions):
            self.assertEqual(part_2(), 3)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
