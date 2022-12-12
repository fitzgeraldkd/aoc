import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_01.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 1475)

    def test_part_2(self):
        self.assertEqual(part_2(), 1516)


class TestExamples(unittest.TestCase):

    SAMPLE_DEPTHS = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_part_1(self):
        self.assertEqual(part_1(self.SAMPLE_DEPTHS), 7)

    def test_part_2(self):
        self.assertEqual(part_2(self.SAMPLE_DEPTHS), 5)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
