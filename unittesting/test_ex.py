import unittest
from testprograms.program4 import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Rahul', 50000)

    def test_email(self):
        self.assertEqual(self.employee.email, 'rahul@hcl.com')

    def test_appply_raise(self):
        self.employee.apply_raise(10)
        self.assertEqual(self.employee.salary, 55000)



