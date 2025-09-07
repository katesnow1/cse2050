from linkedlist import Node
import unittest

class TestNode(unittest.TestCase):
    def test_init_one(self):
        n1 = Node('jake')

        self.assertEqual(n1.data, 'jake')
        self.assertEqual(n1.link, None)

    def test_init_three(self):
        n1 = Node('jake')
        n2 = Node('rachel')
        n3 = Node('cassie')
        
        n1.link = n2
        n2.link = n3
        self.assertIs(n1.link, n2)
        self.assertIs(n2.link, n3)
        self.assertIs(n1.link.link.link, None)

if __name__ == '__main__':
    unittest.main()