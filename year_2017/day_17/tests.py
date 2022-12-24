import unittest

from year_2017.day_17.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 1670)

    def test_part_2(self):
        self.assertEqual(part_2(), 2316253)


class TestExamples(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1(3), 638)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
