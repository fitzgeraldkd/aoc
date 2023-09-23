import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_02.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 7221)

    def test_part_2(self):
        self.assertEqual(part_2(), 'mkcdflathzwsvjxrevymbdpoq')


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        ids = [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab'
        ]
        self.assertEqual(part_1(ids), 12)

    def test_part_2(self):
        ids = [
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz'
        ]
        self.assertEqual(part_2(ids), 'fgij')


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
