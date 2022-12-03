import unittest

import day_01.tests as day_01
import day_02.tests as day_02
import day_03.tests as day_03

TEST_MODULES = [day_01, day_02, day_03]

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for test_module in TEST_MODULES:
        suite.addTests(loader.loadTestsFromTestCase(test_module.TestBase))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
