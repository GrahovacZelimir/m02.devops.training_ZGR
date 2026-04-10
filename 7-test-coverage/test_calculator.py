import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        self.assertRaises(ValueError, calculator.divide, 10, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(calculator.square_root(16), 4)
    def test_square_root_negative(self):
        self.assertRaises(ValueError, calculator.square_root, -1)

    def test_modulo(self):
        self.assertEqual(calculator.modulo(10, 3), 1)
    def test_modulo_by_zero(self):
        self.assertRaises(ValueError, calculator.modulo, 10, 0)
    def test_is_even(self):
        self.assertTrue(calculator.is_even(4))
        self.assertFalse(calculator.is_even(5))

    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)
    def test_factorial_negative(self):
        self.assertRaises(ValueError, calculator.factorial, -1)
    def test_factorial_zero(self):
        self.assertEqual(calculator.factorial(0), 1)
    
    def test_is_positive(self):
        self.assertTrue(calculator.is_positive(5))
        self.assertFalse(calculator.is_positive(-3))
        self.assertFalse(calculator.is_positive(0))


if __name__ == "__main__":
    unittest.main()
