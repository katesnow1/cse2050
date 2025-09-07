from linkedlist import Node, LinkedList
import unittest

class TestNode(unittest.TestCase):
    def setUp(self):
        """Sets up node objects for testing"""
        self.n1 = Node(5)
        self.n2 = Node(6, self.n1)
    def test_init(self):
        """Tests the initiliazation of a new Node object"""
        self.assertEqual(self.n1.item, 5)
        self.assertTrue(self.n1.link is None)
        self.assertEqual(self.n2.item, 6)
        self.assertTrue(self.n2.link == self.n1)
    def test_repr(self):
        """Tests that the repr function prints the correct string representation"""
        self.assertEqual(repr(self.n1), "Node(5)")
        self.assertEqual(repr(self.n2), "Node(6)")

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Sets up the LinkedList objects for testing"""
        self.LL1 = LinkedList([1, 2, 3, 4, 5])
        self.LL2 = LinkedList()

    def assertLinkedList(self, LL, expected_len, expected_head, expected_tail):
        """Tests that the expected length, head, and tail for a LinkedList are all correct"""
        length = len(LL)
        head = LL.get_head()
        tail = LL.get_tail()
        self.assertEqual(length, expected_len)
        self.assertEqual(head, expected_head)
        self.assertEqual(tail, expected_tail)


    def test_init_empty(self):
        """Tests the initialization of an empty LinkedList object"""
        self.assertLinkedList(self.LL2, 0, None, None)

    def test_add_last(self):
        """Tests that a node is added to the end of the LinkedList object"""
        for i in range(10):
            self.LL2.add_last(i)
            self.assertLinkedList(self.LL2, i+1, 0, i)

    def test_init(self):
        """Tests the non-empty initialization of a LinkedList object"""
        self.assertLinkedList(self.LL1, 5, 1, 5)
        
    def test_add_first(self):
        """Tests that a node is added to the front of the LinkedList"""
        for i in range(10):
            self.LL2.add_first(i)
            self.assertLinkedList(self.LL2,i+1, i, 0)

    def test_remove_first(self):
        """Tests that the first Node in a LinkedList can be removed"""
        LL3 = LinkedList([0, 1, 2, 3, 4])
        expectedHead = [1, 2, 3, 4, None]
        expectedTail = [4, 4, 4, 4, None]
        for i in range(len(LL3)):
            if(len(LL3) != 0):
                self.assertEqual(LL3.remove_first(), i)
                self.assertLinkedList(LL3, 4-i, expectedHead[i], expectedTail[i])
        LL3 = LinkedList()
        with self.assertRaises(RuntimeError):
            LL3.remove_first()

    def test_remove_last(self):
        """Tests that the last Node in a LinkedList can be removed"""
        LL4 = LinkedList([0, 1, 2, 3, 4])
        expectedHead = [0, 0, 0, 0, None]
        expectedTail = [3, 2, 1, 0, None]
        for i in range(len(LL4)):
            if(len(LL4) != 0):
                self.assertEqual(LL4.remove_last(), 4-i)
                self.assertLinkedList(LL4, 4-i, expectedHead[i], expectedTail[i])
        LL4 = LinkedList()
        with self.assertRaises(RuntimeError):
            LL4.remove_last()





    #For each, test the following,
    # normal functionality (each thing it updates)


if __name__ == '__main__':
    unittest.main()