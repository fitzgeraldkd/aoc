import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_05.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'VPCDMSLWJ')

    def test_part_2(self):
        self.assertEqual(part_2(), 'TPWCGNCCG')


class TestExamples(unittest.TestCase):
    pass


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
