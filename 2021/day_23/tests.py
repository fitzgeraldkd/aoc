import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_23.solution import find_efficient_path, get_available_positions, part_1, part_2


class TestBase(unittest.TestCase):

    @unittest.expectedFailure
    def test_part_1(self):
        self.assertEqual(part_1(), None)

    @unittest.expectedFailure
    def test_part_2(self):
        self.assertEqual(part_2(), None)


class TestExamples(unittest.TestCase):

    SAMPLE_DIAGRAM = [
        '#############',
        '#...........#',
        '###B#C#B#D###',
        '  #A#D#C#A#',
        '  #########'
    ]

    def test_part_1(self):
        with patch('day_23.solution.read_inputs', return_value=self.SAMPLE_DIAGRAM):
            self.assertEqual(part_1(), 12521)

    def test_part_2(self):
        with patch('day_23.solution.read_inputs', return_value=self.SAMPLE_DIAGRAM):
            self.assertEqual(part_2(), None)


class TestUtils(unittest.TestCase):

    def test_find_efficient_path(self):
        state = {
            'board': {
                (0, 0): 'A',
                (1, 0): None,
                (2, 1): None,
                (2, 2): 'A',
                (3, 0): None,
                (4, 1): 'B',
                (4, 2): 'B',
                (5, 0): None,
                (6, 1): 'C',
                (6, 2): 'C',
                (7, 0): None,
                (8, 1): None,
                (8, 2): 'D',
                (9, 0): None,
                (10, 0): 'D'
            },
            'energy': 0
        }
        self.assertEqual(find_efficient_path(state), 3003)

    """
    Sample map for these tests:
    #############
    #A..D.......#
    ###.#D#C#.###
      #A#B#B#C#
      #########
    """
    def test_get_available_positions(self):
        state = {
            'board': {
                (0, 0): 'A',
                (1, 0): None,
                (2, 1): None,
                (2, 2): 'A',
                (3, 0): 'D',
                (4, 1): 'D',
                (4, 2): 'B',
                (5, 0): None,
                (6, 1): 'C',
                (6, 2): 'B',
                (7, 0): None,
                (8, 1): None,
                (8, 2): 'C',
                (9, 0): None,
                (10, 0): None
            },
            'energy': 0
        }

        self.assertCountEqual(get_available_positions(state, (0, 0)), [(2, 1)])
        self.assertCountEqual(get_available_positions(state, (2, 2)), [])
        self.assertCountEqual(get_available_positions(state, (3, 0)), [])
        self.assertCountEqual(get_available_positions(state, (4, 1)), [(5, 0), (7, 0), (9, 0), (10, 0)])
        self.assertCountEqual(get_available_positions(state, (4, 2)), [])
        self.assertCountEqual(get_available_positions(state, (6, 1)), [(5, 0), (7, 0), (9, 0), (10, 0)])
        self.assertCountEqual(get_available_positions(state, (6, 2)), [])
        self.assertCountEqual(get_available_positions(state, (8, 2)), [(5, 0), (7, 0), (9, 0), (10, 0)])
        self.assertCountEqual(get_available_positions(state, (9, 0)), [])


if __name__ == '__main__':
    unittest.main()
