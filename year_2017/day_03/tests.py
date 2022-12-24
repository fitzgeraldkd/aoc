import unittest

from year_2017.day_03.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 419)

    def test_part_2(self):
        self.assertEqual(part_2(), 295229)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(1), 0)
        self.assertEqual(part_1(12), 3)
        self.assertEqual(part_1(23), 2)
        self.assertEqual(part_1(1024), 31)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
