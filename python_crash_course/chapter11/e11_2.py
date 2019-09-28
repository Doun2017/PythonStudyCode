import unittest
import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.emplayee = Employee.Employee("liu", "shi", 20000)
	def test_give_default_raise(self):
		self.emplayee.give_raise()
		self.assertEqual(self.emplayee.salary, 25000)

	def test_give_custom_raise(self):
		self.emplayee.give_raise(3000)
		self.assertEqual(self.emplayee.salary, 23000)

unittest.main()


