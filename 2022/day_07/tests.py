import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_07.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 1243729)

    def test_part_2(self):
        self.assertEqual(part_2(), 4443914)


class TestExamples(unittest.TestCase):

    SAMPLE_TERMINAL = [
        '$ cd /',
        '$ ls',
        'dir a',
        '14848514 b.txt',
        '8504156 c.dat',
        'dir d',
        '$ cd a',
        '$ ls',
        'dir e',
        '29116 f',
        '2557 g',
        '62596 h.lst',
        '$ cd e',
        '$ ls',
        '584 i',
        '$ cd ..',
        '$ cd ..',
        '$ cd d',
        '$ ls',
        '4060174 j',
        '8033020 d.log',
        '5626152 d.ext',
        '7214296 k'
    ]

    def test_part_1(self):
        with patch('day_07.solution.read_inputs', return_value = self.SAMPLE_TERMINAL):
            self.assertEqual(part_1(), 95437)

    def test_part_2(self):
        with patch('day_07.solution.read_inputs', return_value = self.SAMPLE_TERMINAL):
            self.assertEqual(part_2(), 24933642)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
