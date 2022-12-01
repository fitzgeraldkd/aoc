import unittest

import day_01.tests as day_01

TEST_MODULES = [day_01]

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for test_module in TEST_MODULES:
        suite.addTests(loader.loadTestsFromTestCase(test_module.TestBase))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
