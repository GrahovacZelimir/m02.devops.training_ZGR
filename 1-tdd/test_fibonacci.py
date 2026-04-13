import unittest
from fibonacci import fibonacci


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


if __name__ == "__main__":
    unittest.main()
