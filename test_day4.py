import unittest
from day4 import add_num, power

class TestFunctions(unittest.TestCase):
    def test_add_num(self):
        self.assertEqual(add_num(2, 3), 5)
        self.assertEqual(add_num(-1, 1), 0)

    def test_power(self):
        self.assertEqual(power(2), 4)  # Default exponent (2^2)
        self.assertEqual(power(2, 3), 8)  # Custom exponent (2^3)

if __name__ == "__main__":
    unittest.main()
