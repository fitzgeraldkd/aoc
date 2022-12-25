import unittest
from unittest.mock import patch

from year_2015.day_10.solution import look_and_say, part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 329356)

    def test_part_2(self):
        self.assertEqual(part_2(), 4666278)


class TestExamples(unittest.TestCase):
    pass


class TestUtils(unittest.TestCase):

    def test_look_and_say(self):
        self.assertEqual(look_and_say('1'), '11')
        self.assertEqual(look_and_say('11'), '21')
        self.assertEqual(look_and_say('21'), '1211')
        self.assertEqual(look_and_say('1211'), '111221')
        self.assertEqual(look_and_say('111221'), '312211')


if __name__ == '__main__':
    unittest.main()
