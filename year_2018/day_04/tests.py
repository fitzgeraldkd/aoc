import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_04.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 19025)

    def test_part_2(self):
        self.assertEqual(part_2(), 23776)


class TestExamples(unittest.TestCase):

    SAMPLE_RECORDS = [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up'
    ]

    def test_part_1(self):
        with patch('year_2018.day_04.solution.read_inputs', return_value=self.SAMPLE_RECORDS):
            self.assertEqual(part_1(), 240)

    def test_part_2(self):
        with patch('year_2018.day_04.solution.read_inputs', return_value=self.SAMPLE_RECORDS):
            self.assertEqual(part_2(), 4455)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
