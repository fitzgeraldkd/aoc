import unittest

import day_01.solution as day_01
import day_02.solution as day_02
import day_03.solution as day_03
import day_04.solution as day_04
import day_05.solution as day_05
import day_06.solution as day_06


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


if __name__ == '__main__':
    unittest.main()
