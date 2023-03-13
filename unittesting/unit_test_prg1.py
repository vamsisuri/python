import unittest
import HtmlTestRunner

class My_test(unittest.TestCase):
    def test(self):
        self.assertEqual(3+4,7)
    def test_demo(self):
        self.assertEqual(10+10,20)
    def test_one(self):
        pass

    test_suite=unittest.TestSuite()
    test_suite.addTest(My-test("test"))
    test_suite.addTest("test1")
     testRunner=HtmlTestRunner.HTMLTestRunner(output='reports')
     testRunner.run(test_suite)

