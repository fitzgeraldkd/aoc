import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_07.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'BKCJMSDVGHQRXFYZOAULPIEWTN')

    def test_part_2(self):
        self.assertEqual(part_2(), 1040)


class TestExamples(unittest.TestCase):

    SAMPLE_INSTRUCTIONS = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.'
    ]

    def test_part_1(self):
        with patch('day_07.solution.read_inputs', return_value=self.SAMPLE_INSTRUCTIONS):
            self.assertEqual(part_1(), 'CABDFE')

    def test_part_2(self):
        with patch('day_07.solution.read_inputs', return_value=self.SAMPLE_INSTRUCTIONS), \
                patch('day_07.solution.PART_2_WORKERS', 2), \
                patch('day_07.solution.PART_2_BASE_TIME', 0):
            self.assertEqual(part_2(), 15)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
