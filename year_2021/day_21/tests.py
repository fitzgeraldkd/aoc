import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2021.day_21.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 734820)

    def test_part_2(self):
        self.assertEqual(part_2(), 193170338541590)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1([4, 8]), 739785)

    def test_part_2(self):
        self.assertEqual(part_2([4, 8]), 444356092776315)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
