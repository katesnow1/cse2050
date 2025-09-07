from Graph import Graph
class EdgeSet(Graph):
    def __init__(self, V = None, E = None):
        """Initializes an empty graph"""
        self.V = set()
        self.E = set() # careful! self.E = {} will create a dictionary, not a set
        
        if V is not None:
            for v in V:
                self.add_vertex(v)

        if E is not None:
            for e in E:
                self.add_edge(e)

    def add_vertex(self, v):
        """Adds vertex v to graph"""
        self.V.add(v)

    def add_edge(self, e):
        """Adds edge e to graph"""
        self.E.add(e)

    def neighbors(self, v):
        """returns iterator over neighbors of v. By modifying this function, we
        can make the graph directional or nondirectional.
        """
        for u1, u2 in self.E:
            if u1 == v: yield u2
            elif u2 == v: yield u1


    

if __name__ == '__main__':
    #    2-----3
    #   /      |
    #  /       |
    # 1--------4      5
    
    V = {1, 2, 3, 4, 5}
    E = {(1, 2), (1, 4), (2, 3), (3, 4)}

    G = EdgeSet(V, E)

    assert G.is_connected(1, 4)
    assert G.is_connected(4, 1)
    print("all done!")