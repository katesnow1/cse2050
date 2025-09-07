class Node:
    def __init__(self, data, prev=None, link=None):
        """Initializes a new node"""
        self.data = data
        self.prev = prev
        self.link = link

    def __repr__(self):
        return f"Node({self.data})"
    


class DoublyLinkedList:
    def __init__(self, items=None):
        self._len = 0
        self._head = None
        self._tail = None
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        return self._len

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail
    
    def add_first(self, data):
        #Edge case: 0 item 
        if len(self) == 0:
            self._head = self._tail = Node(data)
        #Edge case : 1+ item list
        else:
            new_node = Node(data, prev=None, link=self._head)
            self._head.prev = new_node #update old head's pointer
            self._head = new_node #update DLL's head

        self._len += 1

    def add_last(self, data):
        #Edge case: 0 item
        if len(self) == 0:
            self._head = self._tail = Node(data)
        else:
            new_node = Node(data, prev=self._tail, link=None)
            self._tail.link = new_node
            self._tail = new_node

        self._len += 1

    def remove_first(self):
        if len(self) == 0: raise IndexError("Cannot remove from empty DLL")
        data = self._head.data
        if len(self) == 1:
            self._tail = self._head = None
        else:
            self._head = self._head.link
            self._head.prev = None

        self._len -= 1
        return data
    
    def remove_last(self):
        data = self._tail.data
        if len(self) == 1:
            self._tail = self._head = None
        else:
            self._tail = self._tail.prev
            self._head.link = None

        self._len -= 1
        return data
        


