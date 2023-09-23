import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2022.day_21.solution import parse_input, part_1, part_2, reverse_value
from utils.setup import read_inputs

CURRENT_DIRECTORY = os.path.realpath(__file__)


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 155708040358220)

    def test_part_2(self):
        self.assertEqual(part_2(), 3342154812537)


class TestExamples(unittest.TestCase):

    @patch('year_2022.day_21.solution.read_inputs', return_value=read_inputs(CURRENT_DIRECTORY, 'sample.txt'))
    def test_part_1(self, mocked_read_inputs):
        self.assertEqual(part_1(), 152)

    @patch('year_2022.day_21.solution.read_inputs', return_value=read_inputs(CURRENT_DIRECTORY, 'sample.txt'))
    def test_part_2(self, mocked_read_inputs):
        self.assertEqual(part_2(), 301)


class TestUtils(unittest.TestCase):

    def test_reverse_value(self):

        instructions = [parse_input(instruction) for instruction in [
            'root: abcd + mnop',
            'abcd: efgh * ijkl',
            'efgh: 5',
            'ijkl: 5',
            'mnop: qrst / uvwx',
            'qrst: 6420',
            'uvwx: 321'
        ]]
        mapped_instructions = { instruction['param']: instruction for instruction in instructions }
        mapped_instructions['root']['value'] = 20
        mapped_instructions['root']['operator'] = '=='
        self.assertEqual(reverse_value(mapped_instructions, 'abcd', 'efgh', 'root'), 4)
        pass


if __name__ == '__main__':
    unittest.main()
