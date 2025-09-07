from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                self.assertTrue(puzzle([2,4,3,1,1,0]))

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                self.assertTrue(puzzle([4,1,3,3,2,0]))

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                self.assertTrue(puzzle([3,6,4,1,1,4,1,0]))
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                self.assertFalse(puzzle([3,4,1,2,0]))

unittest.main()