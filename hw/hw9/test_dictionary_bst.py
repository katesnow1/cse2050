import unittest
from dictionary_bst import Node, DictionaryBST

class TestNode(unittest.TestCase):
    def test_init(self):
        """tests initialiazation of a node"""
        nd = Node("cat", "animal that meows")
        self.assertEqual(nd.word, "cat")
        self.assertEqual(nd.meaning, "animal that meows")
        self.assertIsNone(nd.left)
        self.assertIsNone(nd.right)

class TestBST(unittest.TestCase):
    def test_init(self):
        """tests initialization of a BST"""
        # entries = {"cat":"animal that meows", "dog":"animal that barks", "fish":"animal that swims", "apple":"red food"}
        # dbst = DictionaryBST()
        # self.assertIsNone(dbst._root) #do i have to test this if the attribute it private
        # dbst2 = DictionaryBST(entries)
        # self.assertEqual(dbst2._root, Node())



    def test_insert(self):
        """tests the insertion of a word and its meaning into the tree"""
        dbst = DictionaryBST()
        dbst.insert("cat", "animal that meows")
        self.assertEqual(dbst._head.word, "cat")
        self.assertEqual(dbst._head.meaning, "animal that meows")
        dbst.insert("dog", "animal that barks")
        self.assertEqual(dbst._head.right.word, "dog")
        self.assertEqual(dbst._head.right.meaning, "animal that barks")
        entries = {"cat":"animal that meows", "dog":"animal that barks", "fish":"animal that swims", "apple":"red food", "abc":"zyx"}
        dbst2 = DictionaryBST(entries)
        # self.assertEqual(dbst2._head.word, "dog")
        # self.assertEqual(dbst2._head.left.word, "cat")
        # self.assertEqual(dbst2._head.left.left.word, "apple")
        # self.assertEqual(dbst2._head.right.word, "fish")
        self.assertEqual(dbst2._head.word, "dog")
        self.assertEqual(dbst2._head.left.word, "apple")
        self.assertEqual(dbst2._head.left.left.word, "abc")
        self.assertEqual(dbst2._head.left.right.word, "cat")
        self.assertEqual(dbst2._head.right.word, "fish")


        

    def test_search(self):
        """Tests that searching for a word in the tree returns its meaning"""
        entries = {"cat":"animal that meows", "dog":"animal that barks", "fish":"animal that swims", "apple":"red food"}
        dbst = DictionaryBST(entries)
        self.assertEqual(dbst.search("dog"), "animal that barks")
        self.assertEqual(dbst.search("apple"), "red food")
        self.assertIsNone(dbst.search("carrot"))

        dbst2 = DictionaryBST()
        self.assertIsNone(dbst2.search("dog"))


    def print_alphabetical(self):
        """Tests that all dictionary entries are printed in alphabetical order"""
        entries = {"cat":"animal that meows", "dog":"animal that barks", "fish":"animal that swims", "apple":"red food"}
        dbst = DictionaryBST(entries)
        expected_output = "[(\"apple\", \"red food\"), (\"cat\", \"animal that meows\"), (\"dog\", \"animal that barks\"), (\"fish\", \"animal that swims\")]"
        self.assertEqual(dbst.print_alphabetical(), expected_output)


if __name__ == '__main__':
    unittest.main()