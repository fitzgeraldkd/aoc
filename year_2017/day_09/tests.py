import unittest

from year_2017.day_09.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 16827)

    def test_part_2(self):
        self.assertEqual(part_2(), 7298)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1('{}'), 1)
        self.assertEqual(part_1('{{{}}}'), 6)
        self.assertEqual(part_1('{{},{}}'), 5)
        self.assertEqual(part_1('{{{},{},{{}}}}'), 16)
        self.assertEqual(part_1('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(part_1('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual(part_1('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(part_1('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)

    def test_part_2(self):
        self.assertEqual(part_2('<>'), 0)
        self.assertEqual(part_2('<random characters>'), 17)
        self.assertEqual(part_2('<<<<>'), 3)
        self.assertEqual(part_2('<{!>}>'), 2)
        self.assertEqual(part_2('<!!>'), 0)
        self.assertEqual(part_2('<!!!>>'), 0)
        self.assertEqual(part_2('<{o"i!a,<{i<a>'), 10)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
