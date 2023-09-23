import unittest
import os
import sys
from unittest.mock import call, patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2022.day_10.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 17180)

    @patch('builtins.print')
    def test_part_2(self, mocked_print):
        part_2()

        # Only check the last six print calls to exclude any prints used for debugging.
        self.assertListEqual(mocked_print.call_args_list[-6:], [
            call('###..####.#..#.###..###..#....#..#.###..'),
            call('#..#.#....#..#.#..#.#..#.#....#..#.#..#.'),
            call('#..#.###..####.#..#.#..#.#....#..#.###..'),
            call('###..#....#..#.###..###..#....#..#.#..#.'),
            call('#.#..#....#..#.#....#.#..#....#..#.#..#.'),
            call('#..#.####.#..#.#....#..#.####..##..###..'),
        ])


class TestExamples(unittest.TestCase):

    SAMPLE_INSTRUCTIONS = [
        'addx 15', 'addx -11', 'addx 6', 'addx -3', 'addx 5', 'addx -1', 'addx -8', 'addx 13', 'addx 4', 'noop',
        'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx -35',
        'addx 1', 'addx 24', 'addx -19', 'addx 1', 'addx 16', 'addx -11', 'noop', 'noop', 'addx 21', 'addx -15', 'noop',
        'noop', 'addx -3', 'addx 9', 'addx 1', 'addx -3', 'addx 8', 'addx 1', 'addx 5', 'noop', 'noop', 'noop', 'noop',
        'noop', 'addx -36', 'noop', 'addx 1', 'addx 7', 'noop', 'noop', 'noop', 'addx 2', 'addx 6', 'noop', 'noop',
        'noop', 'noop', 'noop', 'addx 1', 'noop', 'noop', 'addx 7', 'addx 1', 'noop', 'addx -13', 'addx 13', 'addx 7',
        'noop', 'addx 1', 'addx -33', 'noop', 'noop', 'noop', 'addx 2', 'noop', 'noop', 'noop', 'addx 8', 'noop',
        'addx -1', 'addx 2', 'addx 1', 'noop', 'addx 17', 'addx -9', 'addx 1', 'addx 1', 'addx -3', 'addx 11', 'noop',
        'noop', 'addx 1', 'noop', 'addx 1', 'noop', 'noop', 'addx -13', 'addx -19', 'addx 1', 'addx 3', 'addx 26',
        'addx -30', 'addx 12', 'addx -1', 'addx 3', 'addx 1', 'noop', 'noop', 'noop', 'addx -9', 'addx 18', 'addx 1',
        'addx 2', 'noop', 'noop', 'addx 9', 'noop', 'noop', 'noop', 'addx -1', 'addx 2', 'addx -37', 'addx 1', 'addx 3',
        'noop', 'addx 15', 'addx -21', 'addx 22', 'addx -6', 'addx 1', 'noop', 'addx 2', 'addx 1', 'noop', 'addx -10',
        'noop', 'noop', 'addx 20', 'addx 1', 'addx 2', 'addx 2', 'addx -6', 'addx -11', 'noop', 'noop', 'noop'
    ]

    def test_part_1(self):
        with patch('year_2022.day_10.solution.read_inputs', return_value=self.SAMPLE_INSTRUCTIONS):
            self.assertEqual(part_1(), 13140)

    @patch('builtins.print')
    def test_part_2(self, mocked_print):
        with patch('year_2022.day_10.solution.read_inputs', return_value=self.SAMPLE_INSTRUCTIONS):
            part_2()
        self.assertListEqual(mocked_print.call_args_list[-6:], [
            call('##..##..##..##..##..##..##..##..##..##..'),
            call('###...###...###...###...###...###...###.'),
            call('####....####....####....####....####....'),
            call('#####.....#####.....#####.....#####.....'),
            call('######......######......######......####'),
            call('#######.......#######.......#######.....'),
        ])


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
