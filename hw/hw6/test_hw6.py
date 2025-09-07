import unittest
import random
from hw6 import bubble_sort, selection_sort, insertion_sort, merge

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_merge(self):
        """ Test case for the merge function to verify that it correctly merges three sorted rows."""
        # Define the sorted rows to test
        matrix = [[1, 4, 7, 10], [2, 5, 8, 11],[3, 6, 9, 12]] 
        # Expected merged result
        expected_merged = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Call the merge function
        self.assertEqual(expected_merged, merge(matrix[0],matrix[1],matrix[2]))

    def is_sorted(self, L):
        """ Check if a list is sorted. """
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self):
        """tests an empty self"""
        L = [[], [], []]
        sortedList = self.sorting_alg(L)
        self.is_sorted(sortedList[0])
        self.assertEqual(sortedList[1], 0)
    
    def test_sorted(self):
        """tests a sorted list"""
        n = 10
        L = [[i for i in range(n)], [i for i in range(n)], [i for i in range(n)]]
        sortedList = self.sorting_alg(L)
        self.is_sorted(sortedList[0])
        self.assertEqual(sortedList[1], 0)
    
    def test_reverse_sorted(self):
        """tests a reverse-sorted list"""
        n = 10
        L = [[n-i for i in range(n)], [n-i for i in range(n)], [n-i for i in range(n)]]
        sortedList = self.sorting_alg(L)
        self.is_sorted(sortedList[0])
        self.assertEqual(sortedList[1], 45)
    
    def test_random(self):
        """tests a randomly generated list"""
        n = 10
        L = [[random.randint(0, 101) for i in range(n)], [random.randint(0, 101) for i in range(n)], [random.randint(0, 101) for i in range(n)]]
        sortedList = self.sorting_alg(L)
        self.is_sorted(sortedList[0])
    

class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm"""

    def setUp(self):
        """Set up the insertion sort algorithm for testing"""
        super().setUp(insertion_sort)

class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm"""

    def setUp(self):
        """Set up the selection sort algorithm for testing"""
        super().setUp(selection_sort)

    def test_reverse_sorted(self):
        """Tests selection sort on a reverse sorted list"""
        n = 10
        L = [[n-i for i in range(n)], [n-i for i in range(n)], [n-i for i in range(n)]]
        sortedList = selection_sort(L)
        self.is_sorted(sortedList[0])
        self.assertEqual(sortedList[1], 5)
    
    def test_random(self):
        """tests selection sort on a randomly sorted list"""
        n = 10
        L = [[random.randint(0, 101) for i in range(n)], [random.randint(0, 101) for i in range(n)], [random.randint(0, 101) for i in range(n)]]
        sortedList = selection_sort(L)
        self.is_sorted(sortedList[0])

if __name__ == "__main__":
    unittest.main()
