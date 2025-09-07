class Node:
    def __init__(self, item, link=None):
        """Initializes a new Node object, params item and link (link is optional and defaults to None)"""
        self.item = item
        self.link = link
    def __repr__(self):
        """Returns the string representation of the Node object in form Node(item)"""
        return f"Node({self.item})"
    
class LinkedList:
    def __init__(self, items = None):
        """Initializes a LinkedList object with param items"""
        self._head = None 
        self._tail = None
        self._len = 0
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """Returns the length of the LinkedList"""
        return self._len
    
    def get_head(self):
        """Returns the head of the LinkedList, returns None if list is empty"""
        if (len(self) == 0):
            return None
        else:
            return self._head.item
    
    def get_tail(self):
        """Returns the tail of the LinkedList, returns None if list is empty"""
        if (len(self) == 0):
            return None
        else:
            return self._tail.item
    
    def add_last(self, item):
        """Adds Node(item) to the end of the LinkedList, updates tail and len; accounts for empty edge case"""
        n = Node(item)
        if self._head is None: #edge case
            self._head = self._tail = n
        else:
            self._tail.link = n
            self._tail = self._tail.link
        self._len += 1

    def add_first(self, item):
        """Adds Node(item) to the start of the LinkedList, updates head and len; accounts for empty edge case"""
        if self._head is None:
            self.add_last(item)
        else:
            self._head = Node(item, self._head)
            self._len += 1

    def remove_last(self):
        """Removes the last node from the LinkedList and returns its item"""
        if self._head is None:
            raise RuntimeError("Can't remove from linked list")
        item = self._tail.item
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            curr = self._head
            while(curr.link is not self._tail):
                curr = curr.link
            #curr is penultimate element
            self._tail = curr
            self._tail.link = None
        self._len -= 1    
        return item

    def remove_first(self):
        """Removes the first node from the LinkedList and returns its item"""
        if self._len <= 1:
            return self.remove_last()
        item = self._head.item
        self._head = self._head.link
        self._len -= 1
        return item
