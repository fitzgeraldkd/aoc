import unittest

import day_01.solution as day_01
import day_02.solution as day_02
import day_03.solution as day_03
import day_04.solution as day_04


class Test2016Challenges(unittest.TestCase):

    def test_day_1(self):
        self.assertEqual(day_01.part_1(), 242)
        self.assertEqual(day_01.part_2(), 150)

    def test_day_2(self):
        self.assertEqual(day_02.part_1(), '47978')
        self.assertEqual(day_02.part_2(), '659AD')

    def test_day_3(self):
        self.assertEqual(day_03.part_1(), 869)
        self.assertEqual(day_03.part_2(), 1544)

    def test_day_4(self):
        self.assertEqual(day_04.part_1(), 278221)
        self.assertEqual(day_04.part_2(), 267)


if __name__ == '__main__':
    unittest.main()
