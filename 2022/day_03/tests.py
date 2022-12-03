import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_03.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 7908)

    def test_part_2(self):
        self.assertEqual(part_2(), 2838)


class TestExamples(unittest.TestCase):

    SAMPLE_RUCKSACKS = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw'
    ]

    def test_part_1(self):
        self.assertEqual(part_1(self.SAMPLE_RUCKSACKS), 157)

    def test_part_2(self):
        self.assertEqual(part_2(self.SAMPLE_RUCKSACKS), 70)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
