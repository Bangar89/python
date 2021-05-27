import sys
import unittest

#sys.path.append('../src')
sys.path.insert(0, '../src')

loader = unittest.TestLoader()
testSuite = loader.discover('test')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)