from stack import Stack
import unittest

# TDD: Test the public interface
class TestStack(unittest.TestCase):
    def test_init(self):
        """Creates an empty stack and tests length and is_empty()"""
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())

    def test_push_pop(self):
        """Adds 10 items, then removes them."""
        s = Stack()
        n = 10

        for i in range(n):
            s.push(i) # add i to the stack
            self.assertEqual(len(s), i+1)
            self.assertFalse(s.is_empty())
            self.assertEqual(s.peek(), i)

        for i in range(n):
            self.assertFalse(s.is_empty())
            self.assertEqual(s.peek(), n-1-i)
            self.assertEqual(s.pop(), n-1-i)
            self.assertEqual(len(s), n-i-1)
            

        self.assertTrue(s.is_empty())

    def test_peek_empty(self):
        """Peeks from empty stack should raise RuntimeError"""
        s = Stack()

        with self.assertRaises(IndexError):
            s.peek()
            


unittest.main()