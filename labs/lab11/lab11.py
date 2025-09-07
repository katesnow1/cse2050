class Graph_ES:
    def __init__(self, V=None, E=None):
        """initializes a edge set graph"""
        self.V = set()
        self.E = set()
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __len__(self):
        """returns number of vertices in graph"""
        return len(self.V)

    def __iter__(self):
        """iterates over all vertices"""
        return iter(self.V)

    def add_vertex(self, v):
        """adds vertex v to graph"""
        self.V.add(v)

    def remove_vertex(self, v):
        """removes vertex v from graph, raises KeyError if v is not in graph"""
        if v not in self.V:
            raise KeyError(f"Cannot remove, vertex {v} is not in graph")
        else:
            self.V.remove(v)

    def add_edge(self, e):
        """adds edge e to graph"""
        self.E.add(e)

    def remove_edge(self, e):
        """removes edge e from graph, raises KeyError if e is not in graph"""
        if e not in self.E:
            raise KeyError(f"Cannot remove, edge {e} is not in graph")
        else: 
            self.E.remove(e)

    def _neighbors(self, v):
        """returns iterable collection of neighbors of vertex v"""
        nbrs = set()
        for e in self.E:
            #every e is going to be in form (a,b)
            # if a==v, then we know b is a neighbor
            if e[0] == v:
                nbrs.add(e[1])
        return nbrs


class Graph_AS:
    def __init__(self, V=None, E=None):
        """initializes a edge set graph"""
        self.V = set()
        self.nbrs = {} # pairs of 
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __len__(self):
        """returns number of vertices in graph"""
        return len(self.V)

    def __iter__(self):
        """iterates over all vertices"""
        return iter(self.V)

    def add_vertex(self, v):
        """adds vertex v to graph"""
        self.V.add(v)

    def remove_vertex(self, v):
        """removes vertex v from graph, raises KeyError if v is not in graph"""
        if v not in self.V:
            raise KeyError(f"Cannot remove, vertex {v} is not in graph")
        else:
            self.V.remove(v)

    def add_edge(self, e):
        """adds edge e to graph"""
        u,v = e
        if u in self.nbrs: #if its already a key
            self.nbrs[u].add(v)
        else:
            self.nbrs[u] = {v}

    def remove_edge(self, e):
        """removes edge e from graph, raises KeyError if e is not in graph"""
        u,v = e
        if u not in self.nbrs or v not in self.nbrs[u]: #boolean shortcircuiting
            raise KeyError(f"Cannot remove, edge {e} is not in graph")
        self.nbrs[u].remove(v)


    def _neighbors(self, v):
        """returns iterable collection of neighbors of vertex v"""
        return self.nbrs[v]

