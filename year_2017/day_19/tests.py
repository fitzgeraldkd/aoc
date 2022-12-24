import unittest

from year_2017.day_19.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'PBAZYFMHT')

    def test_part_2(self):
        self.assertEqual(part_2(), 16072)


class TestExamples(unittest.TestCase):

    RAW_MAP = [
        '     |          ',
        '     |  +--+    ',
        '     A  |  C    ',
        ' F---|----E|--+ ',
        '     |  |  |  D ',
        '     +B-+  +--+ ',
        '                '
    ]

    def test_part_1(self):
        self.assertEqual(part_1(self.RAW_MAP), 'ABCDEF')

    def test_part_2(self):
        self.assertEqual(part_2(self.RAW_MAP), 38)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
