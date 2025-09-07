class Node:
    def __init__(self, data, link=None):
        """Initializes a new node"""
        self.data = data
        self.link = link

    def __repr__(self):
        return f"Node({self.data})"
    
class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add_first(self, data):
        # node = Node(data, link=None)
        # self._head = node
        self._head = Node(data, link=self._head)
        self._len += 1
    
    def __len__(self):
        return self._len

    def get_head(self):
        return self._head
    
    def remove_first(self):
        #Extract my data
        data = self._head.data
        #update my linked list
        self._head = self._head.link
        self._len -= 1
        #return data
        return data