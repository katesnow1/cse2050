class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.height = 0

    def update_height(self):
        hl = self.left.height if self.left else -1
        hr = self.right.height if self.right else -1
        return max(hl, hr) + 1
    
    def put(self, key, value):
        if self.key == key:
            self.value = value
            return self
        elif key < self.key:
            self.left = self.left.put(key, value) if self.left else Node(key, value)
        elif key > self.key:
            self.right = self.right.put(key, value) if self.right else Node(key, value)

        self.update_height()

        hl = self.left.height if self.left else -1
        hr = self.right.height if self.right else -1
        misbalance = hl - hr

        if misbalance > 1: #left too heavy
            h_outer = self.left.left.height if self.left.left else -1
            h_inner = self.left.right.height if self.left.right else -1
            if h_inner > h_outer:
                self.left = self.left.rotate_left()
            
            return self.rotate_right()
        
        elif misbalance < -1: #right too heavy
            h_outer = self.right.right.height if self.right.right else -1
            h_inner = self.right.left.height if self.right.left else -1
            if h_inner > h_outer:
                self.right = self.right.rotate_right()

            return self.rotate_left()
        
        return self

    def get(self, key):
        if self.key == key:
            return self.value
        elif key < self.key:
            if self.left: return self.left.get(key)
        elif key > self.right:
            if self.right: return self.right.get(key)
        
        raise KeyError(f"Cannot find key {key}.")

    def remove(self, key): #DO NOT KNOW
        if self.key == key:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                max_left = self.left.max_node()
                self._swap(max_left)
                self.left = self.left.remove(key)

        elif key < self.key:
            self.left = self.left.remove(key)
        
        else:
            self.right = self.right.remove(key)

        return self

                
        

    def rotate_left(self):
        old_root, new_root = self, self.right
        old_root.right = new_root.left
        new_root.left = old_root
        old_root.update_height()
        new_root.update_height()
        return new_root

    def rotate_right(self):
        old_root, new_root = self, self.left
        old_root.left = new_root.right
        new_root.right = old_root
        old_root.update_height()
        new_root.update_height()
        return new_root

    def max_node(self):
        if self.right:
            return self.right.max_node()
        else:
            return self

    def preorder(self):
        yield self.key, self.value
        if self.left: yield from self.left.preorder()
        if self.right: yield from self.right.preorder()

    def postorder(self):
        if self.left: yield from self.left.postorder()
        if self.right: yield from self.right.postorder()
        yield self.key, self.value

    def inorder(self):
        if self.left: yield from self.left.inorder()
        yield self.key, self.value
        if self.right: yield from self.right.inorder()

    def _swap(self, other):
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value


class BST:
    def __init__(self, entries):
        #entries = [(key, value)]
        self._root = None
        for entry in entries:
            key, value = entry
            self.put(key, value)


    def put(self, key, value):
        if self._root:
            return self._root.put(key, value)
        else:
            self._root = Node(key, value)

    def get(self, key):
        if self._root:
            return self._root.get(key)
        raise KeyError(f"Cannot find key {key}.")


    def remove(self, key):
        if self._root:
            return self._root.remove(key)
        
        raise KeyError(f"Cannot find key {key}.")

    def preorder(self):
        if self._root:
            yield from self._root.preorder()

    def postorder(self):
        if self._root:
            yield from self._root.postorder()

    def inorder(self):
        if self._root:
            yield from self._root.inorder()


