from factorial import factorial
import unittest

# red
# write tests
# run them to verify failure
# green
# write code till all unittests pass

class TestFactorial(unittest.TestCase):
    def test_basic(self):
        """Tests expected behavior with normal inputs"""
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        """factorial(0) should be 1"""
        self.assertEqual(factorial(0), 1)

    def test_negative(self):
        """factorials isn't well defined on negative
        numbers, so we raise a value error"""
        with self.assertRaises(ValueError):
            factorial(-1)
        #self.assertEqual(factorial(-1), ValueError)

unittest.main()