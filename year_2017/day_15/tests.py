import unittest

from year_2017.day_15.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 600)

    def test_part_2(self):
        self.assertEqual(part_2(), 313)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1([65, 8921]), 588)

    def test_part_2(self):
        self.assertEqual(part_2([65, 8921]), 309)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
