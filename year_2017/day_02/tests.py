import unittest

from year_2017.day_02.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 42378)

    def test_part_2(self):
        self.assertEqual(part_2(), 246)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        example_spreadsheet = [
            [5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]
        ]
        self.assertEqual(part_1(example_spreadsheet), 18)

    def test_part_2(self):
        example_spreadsheet = [
            [5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5]
        ]
        self.assertEqual(part_2(example_spreadsheet), 9)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
