import unittest

from year_2017.day_11.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 696)

    def test_part_2(self):
        self.assertEqual(part_2(), 1461)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(['ne', 'ne', 'ne']), 3)
        self.assertEqual(part_1(['ne', 'ne', 'sw', 'sw']), 0)
        self.assertEqual(part_1(['ne', 'ne', 's', 's']), 2)
        self.assertEqual(part_1(['se', 'sw', 'se', 'sw', 'sw']), 3)

        self.assertEqual(part_1(['ne', 'se']), 2)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
