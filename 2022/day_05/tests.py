import os
import sys
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_05.solution import part_1, part_2
from utils.setup import read_inputs


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'VPCDMSLWJ')

    def test_part_2(self):
        self.assertEqual(part_2(), 'TPWCGNCCG')


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('day_05.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')):
            self.assertEqual(part_1(), 'CMZ')

    def test_part_2(self):
        with patch('day_05.solution.read_inputs', return_value=read_inputs(__file__, 'sample.txt')):
            self.assertEqual(part_2(), 'MCD')


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
