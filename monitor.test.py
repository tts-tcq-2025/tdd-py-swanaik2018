import unittest
from string_calculator import add

class StringCalculatorTest(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)

if __name__ == "__main__":
    unittest.main()
