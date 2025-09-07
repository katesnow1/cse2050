#For Lecture, 11/18/24, yipee!

class Graph: 
    """Goal is to implement, a unweighted, directional graph; let's start with edge set implementation"""
    def __init__(self, V, E):
        """
        Initialize Graph
        args:
        - V: iterable of vertex objects
        - E: iterable of edges (2-tuples of vertices)
        returns:
        - Nothing lol
        """
        self.V = set()
        self.E = set()
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for u,v in E:
                self.add_edge(u,v)
    
    def __len__(self):
        """Magic method for len(self); returns # of vertices"""
        return len(self.V)
        
    def vertices(self):
        """Returns iterable of all vertices"""
        return iter(self.V)
    
    def edges(self): 
        """Returns iterable of all edges"""
        return iter(self.E)
    
    def add_vertex(self, v):
        """Adds new vertex to graph
        args:
        - v: new vertex to be added"""
        self.V.add(v)
        
    def add_edge(self, u, v):
        """Adds new edge to graph
        args:
        - u,v: two vertices to be connected by edge
        
        Raises: 
        - ValueError when u or v is not a vertex ?"""
        if u not in self or v not in self:
            raise ValueError(f'Edge ({u},{v}) must be composed of vertices already in the Graph')
        self.E.add((u,v))
        self.E.add((v,u))
    
    def remove_edge(self, u, v):
        """Removes existing edge from graph
        args:
        - u,v: vertices that specify edge to be removed
        Raises
        - ValueError when (u,v) isn't already an edge
        """
        if (u,v) not in self.E: raise ValueError("Edge should already be in the Graph before removing")
        self.E.remove((u,v))
        self.E.remove((v,u))
    
    def __contains__(self, v):
        """Returns True iff v is a vertex in the graph"""
        return v in self.V
    
    def has_edge(self, u, v):
        """Returns true iff edge (u,v) is in the graph"""
        return (u,v) in self.E
    
    def nbrs(self, v):
        """Returns iterable of all (out)neighbors of vertex v"""
        nbrs = set()
        for e in self.E:
            if e[0] == v:
                nbrs.add(e[1])
        return nbrs
    
    
    def is_path(self, V):
        """Return True iff the ordered collection of vertices V form a path."""
        pass
    
    def is_simple_path(self, V):
        """Return True iff the ordered collection of vertices V form a simple path."""
        pass
    
    def is_cycle(self, V):
        """Return True iff the ordered collection of vertices V form a cycle."""
        pass
    
    def is_simple_cycle(self, V):
        """Return True iff the ordered collection of vertices V form a simple cycle."""
        pass
    
    def connected(self, u, v):
        """Returns True iff there exists a path from from vertex u to vertex v"""
        pass


    
    

if __name__ == '__main__':
    #where I will do my informal testing
    V = {1,2,3,4}
    E = {(1,2), (2,3), (3,4), (1,3)}
    G = Graph(V, E)
    r"""Should look like this:
    1-->2
     \  |
      \ |
       ↘↓
    3<--4
    """
    assert len(G) == 4
    for v in V:
        assert v in G
    for u,v in E:
        assert G.has_edge(u,v)
    assert G.nbrs(1) == {2,3}
    
    G.add_vertex(5)
    assert 5 in G
    G.add_edge(2,5)
    
    
    
    
    
        
    