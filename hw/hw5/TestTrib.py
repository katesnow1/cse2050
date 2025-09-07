from trib import trib
import unittest

class TestTrib(unittest.TestCase):
    def test_first_ten(self):
        """Tests the first 10 numbers in the tribonacci series"""
        solutions = {1:0, 2:0, 3:1, 4:1, 5:2, 6:4, 7:7, 8:13, 9:24, 10:44}
        for k in solutions:
            self.assertEqual(trib(k), solutions[k])

    def test_trib_100(self):
        """Tests the 100th number in the tribonacci series"""
        self.assertEqual(trib(100), 28992087708416717612934417)

unittest.main()