import unittest
from unittest.mock import patch

from year_2017.day_20.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 243)

    def test_part_2(self):
        self.assertEqual(part_2(), 648)


class TestExamples(unittest.TestCase):

    def test_part_1(self):

        example_particles = [
            'p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>',
            'p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>'
        ]

        with patch('year_2017.day_20.solution.read_inputs', return_value=example_particles):
            self.assertEqual(part_1(), 0)

    def test_part_2(self):
        example_particles = [
            'p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>',
            'p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>',
            'p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>',
            'p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>'
        ]

        with patch('year_2017.day_20.solution.read_inputs', return_value=example_particles):
            self.assertEqual(part_2(), 1)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
