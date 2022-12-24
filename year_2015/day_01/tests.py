import unittest

from year_2015.day_01.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 138)

    def test_part_2(self):
        self.assertEqual(part_2(), 1771)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1('(())'), 0)
        self.assertEqual(part_1('()()'), 0)
        self.assertEqual(part_1('((('), 3)
        self.assertEqual(part_1('(()(()('), 3)
        self.assertEqual(part_1('))((((('), 3)
        self.assertEqual(part_1('())'), -1)
        self.assertEqual(part_1('))('), -1)
        self.assertEqual(part_1(')))'), -3)
        self.assertEqual(part_1(')())())'), -3)

    def test_part_2(self):
        self.assertEqual(part_2(')'), 1)
        self.assertEqual(part_2('()())'), 5)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
