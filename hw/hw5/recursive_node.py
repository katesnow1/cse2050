###############################################################################
# init, and repr  are implemented for you. You should implement the other     #
# methods recursively.                                                        #
###############################################################################
class Node:
    """Recursively implementes Linked List functionality"""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length of sublist starting at this node"""
        return 1 if self.link is None else 1 + len(self.link)

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist"""
        return self.data if self.link is None else self.link.get_tail()
    
    def add_last(self, data):
        """Recursively adds to end of this sublist"""
        if self.link is None:
            self.link = Node(data, None)
        else:
            self.link.add_last(data)

    def total(self):
        """Recursively adds all items"""
        return self.data if not self.link else self.data + self.link.total()
    
    def remove_last(self):
        """Recursively removes last item in sublist
            Returns a tuple of (new_head, data). The new_head is the
            new head of this sublist after removing the tail.

            OUTPUT
            ------
            new_head, tail_data
                * new_head: Node or None
                    The new link for whatever node called this function
                
                * tail_data: Any
                    The data that was found in the tail node
        """
        #finds the penultimate node
        if self.link is None:
            data = self.data
            return None, data
        new_head, tail_data = self.link.remove_last()
        self.link = new_head
        return self, tail_data


    def reverse(self, prev):
        """Recursively reverse list"""
        #check if self.link exists
        #before this, you must store self.link otherwise you'll lose access
        #want to make self.link = prev
        #when last step is recursion, tail recursion
        head = self if not self.link else self.link.reverse(self)
        self.link = prev
        return head
            