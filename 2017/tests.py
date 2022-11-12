import unittest

import day_01.solution as day_01
import day_02.solution as day_02
import day_03.solution as day_03
import day_04.solution as day_04
import day_05.solution as day_05
import day_06.solution as day_06


class Test2017Challenges(unittest.TestCase):

    def test_day_1(self):
        self.assertEqual(day_01.part_1(), 1097)
        self.assertEqual(day_01.part_2(), 1188)

    def test_day_2(self):
        self.assertEqual(day_02.part_1(), 42378)
        self.assertEqual(day_02.part_2(), 246)

    def test_day_3(self):
        self.assertEqual(day_03.part_1(), 419)
        self.assertEqual(day_03.part_2(), 295229)

    def test_day_4(self):
        self.assertEqual(day_04.part_1(), 466)
        self.assertEqual(day_04.part_2(), 251)

    def test_day_5(self):
        self.assertEqual(day_05.part_1(), 374269)
        self.assertEqual(day_05.part_2(), 27720699)

    def test_day_6(self):
        self.assertEqual(day_06.part_1(), 11137)
        self.assertEqual(day_06.part_2(), 1037)


if __name__ == '__main__':
    unittest.main()
