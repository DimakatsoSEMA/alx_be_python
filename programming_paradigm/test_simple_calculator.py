import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
