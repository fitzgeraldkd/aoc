import unittest
from unittest.mock import patch

from year_2015.day_12.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 119433)

    def test_part_2(self):
        self.assertEqual(part_2(), 68466)


class TestExamples(unittest.TestCase):

    def test_part_1(self):
        with patch('year_2015.day_12.solution.read_inputs', return_value=['[1,2,3]']):
            self.assertEqual(part_1(), 6)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['{"a":2,"b":4}']):
            self.assertEqual(part_1(), 6)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['[[[3]]]']):
            self.assertEqual(part_1(), 3)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['{"a":{"b":4},"c":-1}']):
            self.assertEqual(part_1(), 3)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['{"a":[-1,1]}']):
            self.assertEqual(part_1(), 0)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['[-1,{"a":1}]']):
            self.assertEqual(part_1(), 0)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['[]']):
            self.assertEqual(part_1(), 0)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['{}']):
            self.assertEqual(part_1(), 0)

    def test_part_2(self):
        with patch('year_2015.day_12.solution.read_inputs', return_value=['[1,2,3]']):
            self.assertEqual(part_2(), 6)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['[1,{"c":"red","b":2},3]']):
            self.assertEqual(part_2(), 4)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['{"d":"red","e":[1,2,3,4],"f":5}']):
            self.assertEqual(part_2(), 0)
        with patch('year_2015.day_12.solution.read_inputs', return_value=['[1,"red",5]']):
            self.assertEqual(part_2(), 6)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
