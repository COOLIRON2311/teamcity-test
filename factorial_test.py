import unittest
from factorial import factorial

class FactorialTest(unittest.TestCase):
    def test_factorial1(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial2(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial3(self):
        self.assertEqual(factorial(20), 2432902008176640000)
