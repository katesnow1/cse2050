class Node:
    def __init__(self, data, link=None):
        """Instantiates a new node for a linked list"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length"""
        # base case - the tail node
        if self.link is None:
            return 1
        
        else:
            return 1 + len(self.link)
        
    def count(self, item):
        """Recursively determines how many instances of item are in list"""
        if self.link is None:
            return 1 if self.data == item else 0
        
        count_link = self.link.count(item)

        if self.data == item:
            count_self = 1
        else:
            count_self = 0

        return count_link + count_self
    
        return self.link.count(item) + (1 if self.data == item else 0)

    def add_before(self, old_item, new_item):
        """Adss a node containing new_item just before the first node containing old_item"""
        #base case: I've found old_item
        if self.data == old_item:
            new_node = Node(new_item, link=self)
            return new_node
        else:
            self.link = self.link.add_before(old_item, new_item)

def list_reprs(node):
    """Returns list of string reprs of all nodes starting at node"""
    node_reprs = []

    while node.link is not None:
        node_reprs.append(repr(node))
        node = node.link

    node_reprs.append(repr(node))

    return node_reprs

if __name__ == '__main__':
    # Typically we'd use a LinkedList class to track the head,
    # but doing that manually here for the sake of simplicity.

    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    nd = Node('d')
    ne = Node('e')

    assert(len(na) == 1)

    na.link = nb
    nb.link = nc
    nc.link = nd
    nd.link = ne

    assert (len(na) == 5)

    assert na.count('c') == 1
    ne.link = Node('c')
    assert na.count('c') == 2

    print(list_reprs(na))
    na.add_before('c', 'r')
    print(list_reprs(na))
