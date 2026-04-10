import unittest
from factorial import factorial
from fibonacci import fibonacci


class TestFactorial(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_10(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_of_3(self):
        self.assertEqual(factorial(3), 6)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_of_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_of_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_of_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_of_10(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_of_15(self):
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)


if __name__ == "__main__":
    unittest.main()
