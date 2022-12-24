import unittest

from year_2015.day_04.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 254575)

    def test_part_2(self):
        self.assertEqual(part_2(), 1038736)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1('abcdef'), 609043)
        self.assertEqual(part_1('pqrstuv'), 1048970)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
