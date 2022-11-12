import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))
from unittest import mock

from day_10.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 4480)

    def test_part_2(self):
        self.assertEqual(part_2(), 'c500ffe015c83b60fad2e4b7d59dabc4')


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with mock.patch('day_10.solution.LENGTH', 5):
            self.assertEqual(part_1([3, 4, 1, 5]), 12)


class TestUtils(unittest.TestCase):

    def test_part_2(self):
        self.assertEqual(part_2([]), 'a2582a3a0e66e6e86e3812dcb672a272')
        self.assertEqual(part_2([ord(char) for char in 'AoC 2017']), '33efeb34ea91902bb2f59c9920caa6cd')
        self.assertEqual(part_2([ord(char) for char in '1,2,3']), '3efbe78a8d82f29979031a4aa0b16a9d')
        self.assertEqual(part_2([ord(char) for char in '1,2,4']), '63960835bcdc130f0b66d7ff4f6a5a8e')


if __name__ == '__main__':
    unittest.main()
