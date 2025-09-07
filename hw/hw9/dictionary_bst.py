class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning, left=None, right=None, height=None):
        """Instantiates a new BST node"""
        self.word = word
        self.meaning = meaning
        self.left = left
        self.right = right
        self.height = height
        self.update_height()

    def __repr__(self):
        return f"BSTNode({self.word}, {self.meaning})"

    def insert(self, word, meaning):
        """helper method that does the actual work for the insert method"""
        if self.word == word: self.meaning = meaning

        elif word < self.word:
            if self.left is not None:
                self.left = self.left.insert(word, meaning)
            else:
                self.left = Node(word, meaning)
        else:
            if self.right is not None:
                self.right = self.right.insert(word, meaning)
            else:
                self.right = Node(word, meaning)
        
        self.update_height()


        hl = self.left.height if self.left else -1
        hr = self.right.height if self.right else -1
        misbalance = hl - hr

        if misbalance < -1:
            h_inner = self.right.left.height if self.right.left else -1
            h_outer = self.right.right.height if self.right.right else -1
            if h_inner > h_outer: self.right = self.right.rotate_right()
            new_root = self.rotate_left()

        elif misbalance > 1:
            h_inner = self.left.right.height if self.left.right else -1
            h_outer = self.left.left.height if self.left.left else -1
            if h_inner > h_outer: self.left = self.left.rotate_left()
            new_root = self.rotate_right()

        else:
            new_root = self

        return new_root


    def update_height(self):
        """Calculates number of edges to reach deepest leaf from here"""
        if self.left is not None:
            hl = self.left.height
        else:
            hl = -1

        if self.right is not None:
            hr = self.right.height
        else:
            hr = -1
        # hl = self.left.height if self.left is not None else -1
        # hr = self.right.height if self.right is not None else -1
        self.height = 1 + max(hl, hr)

    
    def rotate_right(self):
        """Rotates self (down and) to the right"""
        old_head, new_head = self, self.left

        old_head.left = new_head.right
        
        new_head.right = old_head

        self.update_height()
        new_head.update_height()

        return new_head
    
    def rotate_left(self):
        """Rotates self (down and) to the left"""
        old_head, new_head = self, self.right

        old_head.right = new_head.left

        new_head.left = old_head

        self.update_height()
        new_head.update_height()

        return new_head
    
    def search(self, word):
        """Does all the work for the search method in the DictionaryBST class"""
        if word == self.word: return self.meaning

        elif word < self.word:
            if self.left is not None:
                return self.left.search(word)
            
        elif word > self.word: 
            if self.right is not None:
                return self.right.search(word)
            
        return None
    
    def in_order(self):
        """Generator based iteration. We can return items as soon as we find them,
        and the recursive stack we've built stays in memory until the next call
        due to the `yield` keyword.
        """
        if self.left is not None: yield from self.left.in_order()   # recursively go left
        yield (self.word, self.meaning)                                                  # return this word
        if self.right is not None: yield from self.right.in_order() # recursively go right



class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self._head = None
        if entries is not None:
            for word in entries:
                    self.insert(word, entries[word])

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        if self._head is None:
            self._head = Node(word, meaning)
            self._head.update_height()
        else:
            self._head = self._head.insert(word, meaning)


    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        if self._head is not None:
            return self._head.search(word)
        else:
            return None
    
    def in_order(self):
        """generator based iteration for in_order traversal"""
        yield from self._head.in_order()

    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        if self._head is not None:
            gen = self.in_order()
            L = []
            for node in gen:
                L.append(node)
            return L
        else:
            return "Tree is empty"

    # Feel free to implement other helper and private methods

if __name__ == '__main__':
    dbst = DictionaryBST()
    print(dbst.print_alphabetical())
