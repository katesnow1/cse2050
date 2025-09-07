# Import what you need
import unittest
from RecordsMap import LocalRecord, RecordsMap
import random
# Include unittests here. Focus on readability, including comments and docstrings.

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """test the initlization of a LocalRecord object"""
        LR = LocalRecord((95,6), 43, 12, 1)
        self.assertEqual(LR.pos, (95,6))
        self.assertEqual(LR.max, 43)
        self.assertEqual(LR.min, 12)
        self.assertEqual(LR.precision, 1)
        LR2 = LocalRecord((25,7654))
        self.assertEqual(LR2.pos, (25, 7654))
        self.assertIsNone(LR2.max)
        self.assertIsNone(LR2.min)
        self.assertEqual(LR2.precision, 0)


    def test_hash(self):
        """tests that the hash function returns a hash object based on its position"""
        LR = LocalRecord((95,6))
        self.assertEqual(hash(LR), hash((95,6)))

    def test_eq(self):
        """tests that eq will return true iff two records are the same position"""
        LR = LocalRecord((45.1234,61.4291))
        LR2 = LocalRecord((45.4234,61.2291))
        LR3 = LocalRecord((45.7234,61.2291))
        self.assertTrue(LR == LR2)
        self.assertFalse(LR == LR3)


    def test_add_report(self):
        """test that a temperature report is added and updates max and min if neccesary"""
        LR = LocalRecord((95,6))
        LR.add_report(80)
        self.assertEqual(LR.max, 80)
        self.assertEqual(LR.min, 80)
        LR.add_report(90)
        self.assertEqual(LR.max, 90)
        self.assertEqual(LR.min, 80)
        LR.add_report(10)
        self.assertEqual(LR.max, 90)
        self.assertEqual(LR.min, 10)


        


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """test that one report is added to the RecordsMap"""
        RM = RecordsMap()
        pos = (56,32)
        RM.add_report(pos, 80)
        self.assertEqual(len(RM), 1) #test len
        self.assertEqual(RM[pos], (80, 80)) #test get
        self.assertTrue(pos in RM) # test contains


    def test_add_many_reports(self):
        """tests adding many reports to the RecordsMap"""
        RM = RecordsMap()
        n = 100
        i=0
        while i < n:
            pos = (random.randrange(0, 171) + random.random(), random.randrange(0, 171) + random.random())
            temp = random.randrange(0, 100)
            if pos in RM: #checks for the conditional where a duplicate position is added to the RecordsMap
                continue

            RM.add_report(pos, temp)
            self.assertEqual(len(RM), i+1)
            self.assertEqual(RM[pos], (temp, temp))
            self.assertTrue(pos in RM)
            i+=1


            


# You need to add a line here to run the unittests

if __name__ == '__main__':
    unittest.main()