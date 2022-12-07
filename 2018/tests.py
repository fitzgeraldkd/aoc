import unittest

import day_01.tests as day_01
import day_02.tests as day_02
import day_03.tests as day_03
import day_04.tests as day_04
import day_05.tests as day_05
import day_06.tests as day_06
import day_07.tests as day_07
import day_08.tests as day_08

TEST_MODULES = [day_01, day_02, day_03, day_04, day_05, day_06, day_07, day_08]

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for test_module in TEST_MODULES:
        suite.addTests(loader.loadTestsFromTestCase(test_module.TestBase))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
