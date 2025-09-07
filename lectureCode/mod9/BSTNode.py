class BSTNode:
    def __init__(self, key, value, left=None, right=None):
        """Instantiates a new BST node"""
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def put(self, key, value):
        """Adds k:v pair to mapping or updates value if k already in mapping"""
        # base case - this is the key we are looking for
        if key == self.key: self.value = value

        elif key < self.key: #go left
            if self.left is None:
                self.left = BSTNode(key, value)
            else:
                self.left.put(key, value)

        else: #go right
            if self.right is None:
                self.right = BSTNode(key, value)
            else:
                self.right.put(key, value)

    def get(self, key):
        """Returns value associated with key"""
        #base case - this is the key
        if key == self.key: return self.value

        elif key < self.key:
            if self.left is not None:
                return self.left.get(key)
            
        elif key > self.key:
            if self.right is not None:
                return self.right.get(key)
            
        raise KeyError(f"Key {key} not found")

    def __repr__(self):
        """Returns string repr of just this node"""
        return f"BSTNode({self.key}, {self.value})"
    
    def __contains__(self, key):
        """returns true if key in mapping"""
        if key == self.key: return True
        elif key < self.key:
            if self.left is not None:
                return key in self.left
        elif key > self.key:
            if self.right is not None:
                return key in self.right
        
        return False

if __name__ == '__main__':
    root = BSTNode('jake', 0)
    assert root.get('jake') == 0
    assert 'jake' in root
    assert 'rachel' not in root

    root.put('rachel', 1)
    assert root.get('jake') == 0
    assert root.get('rachel') == 1
    assert 'rachel' in root
    print("all good")