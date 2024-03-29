import unittest

import year_2017.day_01.tests as day_01
import year_2017.day_02.tests as day_02
import year_2017.day_03.tests as day_03
import year_2017.day_04.tests as day_04
import year_2017.day_05.tests as day_05
import year_2017.day_06.tests as day_06
import year_2017.day_07.tests as day_07
import year_2017.day_08.tests as day_08
import year_2017.day_09.tests as day_09
import year_2017.day_10.tests as day_10
import year_2017.day_11.tests as day_11
import year_2017.day_12.tests as day_12
import year_2017.day_13.tests as day_13
import year_2017.day_14.tests as day_14
import year_2017.day_15.tests as day_15
import year_2017.day_16.tests as day_16
import year_2017.day_17.tests as day_17
import year_2017.day_18.tests as day_18
import year_2017.day_19.tests as day_19
import year_2017.day_20.tests as day_20
import year_2017.day_21.tests as day_21
import year_2017.day_22.tests as day_22
import year_2017.day_23.tests as day_23
import year_2017.day_24.tests as day_24
import year_2017.day_25.tests as day_25

TEST_MODULES = [
    day_01, day_02, day_03, day_04, day_05,
    day_06, day_07, day_08, day_09, day_10,
    day_11, day_12, day_13, day_14, day_15,
    day_16, day_17, day_18, day_19, day_20,
    day_21, day_22, day_23, day_24, day_25
]


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for test_module in TEST_MODULES:
        suite.addTests(loader.loadTestsFromTestCase(test_module.TestBase))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
