import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from year_2022.day_11.solution import part_1, part_2


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 55458)

    def test_part_2(self):
        self.assertEqual(part_2(), 14508081294)


class TestExamples(unittest.TestCase):

    SAMPLE_MONKEYS = [
        'Monkey 0:',
            'Starting items: 79, 98',
            'Operation: new = old * 19',
            'Test: divisible by 23',
                'If true: throw to monkey 2',
                'If false: throw to monkey 3',
        '\n',
        'Monkey 1:',
            'Starting items: 54, 65, 75, 74',
            'Operation: new = old + 6',
            'Test: divisible by 19',
                'If true: throw to monkey 2',
                'If false: throw to monkey 0',
        '\n',
        'Monkey 2:',
            'Starting items: 79, 60, 97',
            'Operation: new = old * old',
            'Test: divisible by 13',
                'If true: throw to monkey 1',
                'If false: throw to monkey 3',
        '\n',
        'Monkey 3:',
            'Starting items: 74',
            'Operation: new = old + 3',
            'Test: divisible by 17',
                'If true: throw to monkey 0',
                'If false: throw to monkey 1'
    ]

    def test_part_1(self):
        with patch('year_2022.day_11.solution.read_inputs', return_value=self.SAMPLE_MONKEYS):
            self.assertEqual(part_1(), 10605)

    def test_part_2(self):
        with patch('year_2022.day_11.solution.read_inputs', return_value=self.SAMPLE_MONKEYS):
            self.assertEqual(part_2(), 2713310158)


class TestUtils(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
