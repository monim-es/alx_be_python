import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
