import queue
class Graph:
    def __init__(self, V=None, E=None):
        """Raises NotImplemented Error"""
        raise NotImplementedError("Please specify between Adjacency Set Graph or Edge Set Graph")

    def is_connected(self, v1, v2):
        """returns True if there is a path between v1 and v2, false otherwise"""
        return self._is_connected(v1, v2, visited=set())
        
    def _is_connected(self, v1, v2, visited):
        """returns True if there is a path between v1 and v2, false otherwise"""
        if v1 in visited: return False
        else: visited.add(v1)

        if v1 == v2: return True

        return any(self._is_connected(n, v2, visited) for n in self.nbrs(v1))

    def bfs(self, v):
        """returns a breadth-first search tree"""
        tree = {}
        to_visit = queue.Queue()
        to_visit.put((v, None))
        while not to_visit.empty():
            child, parent = to_visit.get()
            if child not in tree:
                tree[child] = parent
                for n in self.nbrs(child):
                    if n not in tree:
                        to_visit.put((n, child))

        return tree


    def shortest_path(self, v1, v2):
        """returns shortest path between v1 and v2"""
        bfs_tree = self.bfs(v2)
        path = [v1]
        node = v1
        while bfs_tree[node] is not None:
            node = bfs_tree[node]
            path.append(node)
        return path


    def count_trees(self):
        """returns a list of distinct trees in a graph as well as the number of trees"""
        return self._count_trees(visited = set())

    def _count_trees(self, visited):
        """returns a list of distinct trees in a graph as well as the number of trees"""
        trees = []
        count = 0
        for vertex in self:
            if vertex not in visited:
                tree = self.bfs(vertex)
                trees.append(tree)
                for v in tree:
                    visited.add(v)
                count += 1
        return trees, count



class AdjacencySetGraph(Graph):
    def __init__(self, V=None, E=None):
        """Initilizes an AdjacencySetGraph with vertices V and edges E"""
        self.V = set()
        self._nbrs = {}
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        """returns an iterator over all vertices in graph"""
        return iter(self.V)

    def add_vertex(self, v):
        """adds a vertex to the graph"""
        self.V.add(v)

    def add_edge(self, e): #make sure this is a non directional graphs
        """adds an edge to the graph"""
        u,v = e
        if u in self._nbrs:
            self._nbrs[u].add(v)
        else:
            self._nbrs[u] = {v}
        if v in self._nbrs:
            self._nbrs[v].add(u)
        else:
            self._nbrs[v] = {u}

    def nbrs(self, v):
        """returns an iterator over all neighbors of v"""
        #return self._nbrs[v]
        if v not in self._nbrs:
            return iter(set())
        return iter(self._nbrs[v])

class EdgeSetGraph(Graph):
    def __init__(self, V=None, E=None):
        """Initilizes an EdgeSetGraph with vertices V and edges E"""
        self.V = set()
        self.E = set()
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        """returns an iterator over all vertices in graph"""
        return iter(self.V)

    def add_vertex(self, v):
        """adds a vertex to the graph"""
        self.V.add(v)

    def add_edge(self, e):
        """adds an edge to the graph"""
        self.E.add(e)
        self.E.add((e[1],e[0]))

    def nbrs(self, v):
        """returns an iterator over all neighbors of v"""
        nbrs = set()
        for e in self.E:
            if e[0] == v:
                nbrs.add(e[1])
        # return nbrs
        return iter(nbrs)


if __name__ == '__main__':
    V = {0,1,2,3,4}
    E = [(0,1),(2,3)]
    g = AdjacencySetGraph(V,E)
    print(g.count_trees())
    
