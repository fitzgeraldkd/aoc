import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from unittest import mock

from day_07.solution import parse_input, part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 'bsfpjtc')

    def test_part_2(self):
        self.assertEqual(part_2(), 529)


class TestExamples(unittest.TestCase):

    example_input = [
        'pbga (66)',
        'xhth (57)',
        'ebii (61)',
        'havc (66)',
        'ktlj (57)',
        'fwft (72) -> ktlj, cntj, xhth',
        'qoyq (66)',
        'padx (45) -> pbga, havc, qoyq',
        'tknk (41) -> ugml, padx, fwft',
        'jptl (61)',
        'ugml (68) -> gyxo, ebii, jptl',
        'gyxo (61)',
        'cntj (57)',
    ]

    def test_part_1(self):
        with mock.patch('day_07.solution.read_inputs', return_value=self.example_input):
            self.assertEqual(part_1(), 'tknk')

    def test_part_2(self):
        with mock.patch('day_07.solution.read_inputs', return_value=self.example_input):
            self.assertEqual(part_2(), 60)


class TestUtils(unittest.TestCase):

    def test_parse_input(self):
        self.assertDictEqual(parse_input('pbga (66)'), {
            'name': 'pbga',
            'weight': 66,
            'parents': []
        })

        self.assertDictEqual(parse_input('fwft (72) -> ktlj, cntj, xhth'), {
            'name': 'fwft',
            'weight': 72,
            'parents': ['ktlj', 'cntj', 'xhth']
        })


if __name__ == '__main__':
    unittest.main()
