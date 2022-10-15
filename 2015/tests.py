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


class Test2015Challenges(unittest.TestCase):

    def test_day_1(self):
        self.assertEqual(day_01.part_1(), 138)
        self.assertEqual(day_01.part_2(), 1771)

    def test_day_2(self):
        self.assertEqual(day_02.part_1(), 1588178)
        self.assertEqual(day_02.part_2(), 3783758)
    
    def test_day_3(self):
        self.assertEqual(day_03.part_1(), 2081)
        self.assertEqual(day_03.part_2(), 2341)
    
    def test_day_4(self):
        self.assertEqual(day_04.part_1(), 254575)
        self.assertEqual(day_04.part_2(), 1038736)
    
    def test_day_5(self):
        self.assertEqual(day_05.part_1(), 258)
        self.fail('Finish day 4 part 2.')
    
    def test_day_6(self):
        self.assertEqual(day_06.part_1(), 569999)
        self.assertEqual(day_06.part_2(), 17836115)
    
    def test_day_7(self):
        self.assertEqual(day_07.part_1(), 3176)
        self.assertEqual(day_07.part_2(), 14710)
    
    def test_day_8(self):
        self.assertEqual(day_08.part_1(), 1333)
        self.assertEqual(day_08.part_2(), 2046)
    
    def test_day_9(self):
        self.assertEqual(day_09.part_1(), 251)
        self.assertEqual(day_09.part_2(), 898)
    
    def test_day_10(self):
        self.assertEqual(day_10.part_1(), 329356)
        self.assertEqual(day_10.part_2(), 4666278)
    
    def test_day_11(self):
        self.assertEqual(day_11.part_1(), 'cqjxxyzz')
        self.assertEqual(day_11.part_2(), 'cqkaabcc')
    
    def test_day_12(self):
        self.assertEqual(day_12.part_1(), 119433)
        self.assertEqual(day_12.part_2(), 68466)
    
    def test_day_13(self):
        self.assertEqual(day_13.part_1(), 709)
        self.assertEqual(day_13.part_2(), 668)
    
    def test_day_14(self):
        self.assertEqual(day_14.part_1(), 2640)
        self.assertEqual(day_14.part_2(), 1102)
    
    def test_day_15(self):
        self.assertEqual(day_15.part_1(), 13882464)
        self.assertEqual(day_15.part_2(), 11171160)
    
    def test_day_16(self):
        self.assertEqual(day_16.part_1(), 103)
        self.assertEqual(day_16.part_2(), 405)
    
    def test_day_17(self):
        self.assertEqual(day_17.part_1(), 4372)
        self.assertEqual(day_17.part_2(), 4)
    
    def test_day_18(self):
        self.assertEqual(day_18.part_1(), 814)
        self.assertEqual(day_18.part_2(), 924)
    
    def test_day_19(self):
        self.assertEqual(day_19.part_1(), 576)
        self.assertEqual(day_19.part_2(), 207)
    
    def test_day_20(self):
        self.assertEqual(day_20.part_1(), 776160)
        self.assertEqual(day_20.part_2(), 786240)
    
    def test_day_21(self):
        self.assertEqual(day_21.part_1(), 111)
        self.assertEqual(day_21.part_2(), 188)


if __name__ == '__main__':
    unittest.main()