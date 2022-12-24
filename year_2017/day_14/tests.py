import unittest

from year_2017.day_14.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 8230)

    def test_part_2(self):
        self.assertEqual(part_2(), 1103)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1('flqrgnkx'), 8108)

    def test_part_2(self):
        self.assertEqual(part_2('flqrgnkx'), 1242)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
