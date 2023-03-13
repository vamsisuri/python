import unittest
import HtmlTestRunner
from testprograms import program1
class My_test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(program1.add_two_numbers(-10,-30),-40)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(-40,3),-37)
    def test_case3(self):
        self.assertEqual(program1.add_two_numbers(50,50),100)

test_suite = unittest.TestSuite()
test_suite.addTest(My_test("test_case1"))
# test_suite.addTest("test1")
testRunner=HtmlTestRunner.HTMLTestRunner(output='reports')
testRunner.run(test_suite)
