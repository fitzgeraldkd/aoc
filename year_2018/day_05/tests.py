import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_05.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 11540)

    def test_part_2(self):
        self.assertEqual(part_2(), 6918)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1('dabAcCaCBAcCcaDA'), 10)

    def test_part_2(self):
        self.assertEqual(part_2('dabAcCaCBAcCcaDA'), 4)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
