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
import day_10.solution as day_10
import day_11.solution as day_11
import day_12.solution as day_12
import day_13.solution as day_13
import day_14.solution as day_14
import day_15.solution as day_15
import day_16.solution as day_16
import day_17.solution as day_17
import day_18.solution as day_18
import day_19.solution as day_19
import day_20.solution as day_20
import day_21.solution as day_21


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

    def test_day_10(self):
        self.assertEqual(day_10.part_1(), 56)
        self.assertEqual(day_10.part_2(), 7847)

    def test_day_11(self):
        self.assertEqual(day_11.part_1(), 33)
        self.assertEqual(day_11.part_2(), 57)

    def test_day_12(self):
        self.assertEqual(day_12.part_1(), 318007)
        self.assertEqual(day_12.part_2(), 9227661)

    def test_day_13(self):
        self.assertEqual(day_13.part_1(), 86)
        self.assertEqual(day_13.part_2(), 127)

    def test_day_14(self):
        self.assertEqual(day_14.part_1(), 25427)
        self.assertEqual(day_14.part_2(), 22045)

    def test_day_15(self):
        self.assertEqual(day_15.part_1(), 148737)
        self.assertEqual(day_15.part_2(), 2353212)

    def test_day_16(self):
        self.assertEqual(day_16.part_1(), '11111000111110000')
        self.assertEqual(day_16.part_2(), '10111100110110100')

    def test_day_17(self):
        self.assertEqual(day_17.part_1(), 'DDURRLRRDD')
        self.assertEqual(day_17.part_2(), 436)

    def test_day_18(self):
        self.assertEqual(day_18.part_1(), 1987)
        self.assertEqual(day_18.part_2(), 19984714)

    def test_day_19(self):
        self.assertEqual(day_19.part_1(), 1834471)
        self.assertEqual(day_19.part_2(), 1420064)

    def test_day_20(self):
        self.assertEqual(day_20.part_1(), 17348574)
        self.assertEqual(day_20.part_2(), 104)

    def test_day_21(self):
        self.assertEqual(day_21.part_1(), 'bfheacgd')
        self.assertEqual(day_21.part_2(), 'gcehdbfa')


if __name__ == '__main__':
    unittest.main()
