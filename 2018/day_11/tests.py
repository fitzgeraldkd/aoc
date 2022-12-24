import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_11.solution import get_power_level, part_1, part_2


class TestBase(unittest.TestCase):

    @unittest.expectedFailure
    def test_part_1(self):
        self.assertEqual(part_1(), None)

    @unittest.expectedFailure
    def test_part_2(self):
        self.assertEqual(part_2(), None)


class TestExamples(unittest.TestCase):
    pass


class TestUtils(unittest.TestCase):

    def test_get_power_level(self):
        self.assertEqual(get_power_level(8, 3, 5), 4)


if __name__ == '__main__':
    unittest.main()
