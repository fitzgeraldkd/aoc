import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2018.day_14.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), '3410710325')

    def test_part_2(self):
        self.assertEqual(part_2(), 20216138)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(9), '5158916779')
        self.assertEqual(part_1(5), '0124515891')
        self.assertEqual(part_1(18), '9251071085')
        self.assertEqual(part_1(2018), '5941429882')

    def test_part_2(self):
        self.assertEqual(part_2('51589'), 9)
        self.assertEqual(part_2('01245'), 5)
        self.assertEqual(part_2('92510'), 18)
        self.assertEqual(part_2('59414'), 2018)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
