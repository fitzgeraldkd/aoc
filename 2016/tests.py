import unittest

import day_01.solution as day_01
import day_02.solution as day_02
import day_03.solution as day_03
import day_04.solution as day_04
import day_05.solution as day_05
import day_06.solution as day_06
import day_07.solution as day_07
import day_08.solution as day_08
import day_09.solution as day_09


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

    def test_day_5(self):
        self.assertEqual(day_05.part_1(), 'f97c354d')
        self.assertEqual(day_05.part_2(), '863dde27')

    def test_day_6(self):
        self.assertEqual(day_06.part_1(), 'qtbjqiuq')
        self.assertEqual(day_06.part_2(), 'akothqli')

    def test_day_7(self):
        self.assertEqual(day_07.part_1(), 110)
        self.assertEqual(day_07.part_2(), 242)

    def test_day_8(self):
        self.assertEqual(day_08.part_1(), 121)
        self.skipTest('Script cannot parse the results as text.')
        self.assertEqual(day_08.part_2(), 'RURUCEOEIL')

    def test_day_9(self):
        self.assertEqual(day_09.part_1(), 115118)
        self.assertEqual(day_09.part_2(), 11107527530)


if __name__ == '__main__':
    unittest.main()
