from linkedlist import Node, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def test_init(self):
        ll1 = LinkedList()
        self.assertEqual(len(ll1), 0)
        self.assertEqual(ll1.get_head, None)

    def test_add_first_one(self):
        ll1 = LinkedList()
        ll1.add_first('jake')
        self.assertEqual(len(ll1), 1)
        self.assertEqual(ll1.get_head.data, 'jake')
        self.assertEqual(ll1.get_head.link, None)

    def test_add_first_ten(self):
        ll1 = LinkedList()
        n = 10
        for i in range(n):
            ll1.add_first(i)
            self.assertEqual(len(ll1), i+1)
            self.assertEqual(ll1.get_head().data, i)

    def test_remove_first_one(self):
        ll1= LinkedList()
        ll1.add_first('jake')
        self.assertEqual(ll1.remove_first(), 'jake')

if __name__ == '__main__':
    unittest.main()