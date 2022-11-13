import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_01.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 1097)

    def test_part_2(self):
        self.assertEqual(part_2(), 1188)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1('1122'), 3)
        self.assertEqual(part_1('1111'), 4)
        self.assertEqual(part_1('1234'), 0)
        self.assertEqual(part_1('91212129'), 9)

    def test_part_2(self):
        self.assertEqual(part_2('1212'), 6)
        self.assertEqual(part_2('1221'), 0)
        self.assertEqual(part_2('123425'), 4)
        self.assertEqual(part_2('123123'), 12)
        self.assertEqual(part_2('12131415'), 4)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
