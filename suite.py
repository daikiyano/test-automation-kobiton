import unittest
class TestRunner(unittest.TestCase):
 
    def test_runner(self):
        test_suite = unittest.TestSuite()
        tests = unittest.defaultTestLoader.discover("test", pattern="test_*.py")
        test_suite.addTest(tests)
        unittest.TextTestRunner().run(test_suite)