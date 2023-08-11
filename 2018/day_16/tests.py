import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from day_16.solution import part_1, part_2, Registers


class TestBase(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1(), 596)

    def test_part_2(self):
        self.assertEqual(part_2(), 554)


class TestExamples(unittest.TestCase):
    pass


class TestUtils(unittest.TestCase):

    def test_addi(self):
        registers = Registers(3, 2, 1, 1)
        registers.addi(2, 1, 2)
        self.assertListEqual(registers.values, [3, 2, 2, 1])

    def test_mulr(self):
        registers = Registers(3, 2, 1, 1)
        registers.mulr(2, 1, 2)
        self.assertListEqual(registers.values, [3, 2, 2, 1])

    def test_seti(self):
        registers = Registers(3, 2, 1, 1)
        registers.seti(2, 1, 2)
        self.assertListEqual(registers.values, [3, 2, 2, 1])


if __name__ == '__main__':
    unittest.main()
