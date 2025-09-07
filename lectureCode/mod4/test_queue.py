from queue import Queue
import unittest

class TestQueue(unittest.TestCase):
    def test_init(self):
        """Creates an empty queue and tests length and is_empty()"""
        q = Queue()
        self.assertEqual(len(q), 0)
        self.assertTrue(q.is_empty())

    def test_enqueue_dequeue(self):
        """Adds 10 items, then removes them."""
        q = Queue()
        n = 10

        for i in range(n):
            q.enqueue(i)
            self.assertFalse(q.is_empty())
            self.assertEqual(len(q), i+1)
            self.assertEqual(q.peek(), 0)

        for i in range(n):
            self.assertEqual(q.peek(), i) # next item is correct
            self.assertEqual(q.dequeue(), i)  # returns correct value
            self.assertEqual(len(q), n-1-i)   # len is updated

        self.assertTrue(q.is_empty())

unittest.main()