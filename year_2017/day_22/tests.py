import unittest

from year_2017.day_22.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 5256)

    def test_part_2(self):
        self.assertEqual(part_2(), 2511345)


class TestExamples(unittest.TestCase):

    INITIAL_STATE = [
        '..#',
        '#..',
        '...'
    ]

    def test_part_1(self):
        self.assertEqual(part_1(self.INITIAL_STATE), 5587)

    def test_part_2(self):
        self.assertEqual(part_2(self.INITIAL_STATE), 2511944)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
