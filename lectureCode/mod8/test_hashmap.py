from hashmap import HashMap
import unittest
import random
random.seed(658)

class TestHashmap(unittest.TestCase):
    def test_initempty(self):
        """Initializes an empty hashmap"""
        hm = HashMap()
        self.assertEqual(len(hm), 0)

    def test_addone(self):
        """Adds a single k:v pair to our hashmap"""
        hm = HashMap()
        hm['jake'] = {'CSE 2050', 'CSE 4939W'}

        self.assertEqual(hm['jake'], {'CSE 2050', 'CSE 4939W'})
        self.assertEqual(len(hm), 1)

    def test_overwrite(self):
        """Overwrites the value of an existing key"""
        hm = HashMap()
        hm['jake'] = {'CSE 2050', 'CSE 4939W'}

        self.assertEqual(hm['jake'], {'CSE 2050', 'CSE 4939W'})
        self.assertEqual(len(hm), 1)

        hm['jake'] = {'CSE 3666'}
        self.assertEqual(hm['jake'], {'CSE 3666'})
        self.assertEqual(len(hm), 1)

    def test_addmany(self):
        """Adds a bunch of key:value pairs"""
        n = 10000
        hm = HashMap()

        for key in range(n):
            hm[key] = str(key)
            self.assertEqual(len(hm), key+1)
            self.assertEqual(hm[key], str(key))

if __name__ == '__main__':
    unittest.main()