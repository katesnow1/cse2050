import unittest
from hw3 import generate_lists, find_common, find_common_efficient, measure_time
class TestHW(unittest.TestCase):
    def test_generate(self):
        """Tests that two lists are generated of correct size
        and contain unique integers"""
        self.assertEqual(len(generate_lists(10)[0]), 10)
        list1 = generate_lists(10)[0]
        self.assertEqual(len(list1), len(set(list1)))

    def test_find_common(self):
        """Tests that the correct number of shared elements is returned"""
        list1 = [0, 1, 6, 9, 10]
        list2 = [1, 4 , 6, 8 , 11]
        self.assertEqual(find_common(list1, list2), 2)

    def test_find_common_efficient(self):
        """Tests that the correct number of shared elements is returned"""
        list1 = [0, 1, 6, 9, 10]
        list2 = [1, 4 , 6, 8 , 11]
        self.assertEqual(find_common_efficient(list1, list2), 2)

unittest.main()