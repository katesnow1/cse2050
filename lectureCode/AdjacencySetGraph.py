from Graph import Graph
class AdjacencySet(Graph):
    """Digraph implementation using Adjacency Set"""
    def __init__(self, V = None, E = None):
        """Initializes an empty graph"""
        self._neighbors = dict() #could use {}
        if V is not None:
            for v in V: self.add_vertex(v)

        if E is not None:
            for e in E: self.add_edge(e)


    def add_vertex(self, v):
        """Adds vertex to graph"""
        if v not in self._neighbors:
            self._neighbors[v] = set()
        
        # dict.setdefault(key, default_value)
        # 1) add key:default_value if key not already in dict
        # 2) return dict[key] regardless
        # self._neighbors.setdefault(v, set())


    def add_edge(self, e):
        """Adds edge to graph"""
        u, v = e[0], e[1]
        self._neighbors[u].add(v)
        self._neighbors[v].add(u)


    def neighbors(self, v):
        """returns iterator over neighbors of v"""
        # o(degree(v))
        return iter(self._neighbors[v])

    

if __name__ == '__main__':
    #    2-----3
    #   /      |
    #  /       |
    # 1--------4      5
    
    V = {1, 2, 3, 4}
    E = {(1, 2), (1, 4), (2, 3), (3, 4)}

    G = AdjacencySet(V, E)

    assert G.is_connected(1, 4)
    assert G.is_connected(4, 1)
    print("all done!")