import queue

class EdgeSet():
    def __init__(self, V, E):
        self.V = set()
        self.E = set()
        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for e in E:
                self.add_edge(e)
        


    def add_vertex(self, v):
        self.V.add(v)

    def add_edge(self, e):
        self.E.add(e)

    def iter(self):
        return iter(self.V)

    def neighbors(self, v):
        nbrs = set()
        for e in self.E:
            if e[0] == v:
                nbrs.add(e[1])
        return nbrs

    def is_connected(self, v1, v2):
        self._is_connected(v1, v2, visited=set())

    def _is_connected(self, v1, v2, visited):
        if v1 in visited:
            return False
        if v1 == v2:
            return True
        visited.add(v1)
        for nbr in self.neighbors(v1):
            return any(self._is_connected(nbr, v2, visited))

    def dfs_recr(self, v1):
        tree = {v1:None}
        self._dfs(v1, tree)
        return tree

    def _dfs(self, v1, tree):
        for nbr in self.neighbors(v1):
            if not nbr in tree:
                tree[nbr] = v1
                self._dfs(nbr, tree)


    def dfs(self, v):
        to_visit = [(None, v)]
        tree = {}
        while len(to_visit) != 0:
            parent, child = to_visit.pop()
            if not child in tree:
                tree[child] = parent
                for nbr in self.neighbors(v):
                    to_visit.append((v, nbr))
        return tree


    def bfs(self, v):
        to_visit = queue.Queue()
        to_visit.put((None, v))
        tree = {}
        while not to_visit.empty():
            parent, child = to_visit.get()
            if not child in tree:
                tree[child] = parent
                for nbr in self.neighbors(v):
                    to_visit.put((v, nbr))
        return tree


class AdjacencySet():
    def __init__(self, V, E):
        self.V = set()
        self.nbrs = {}
        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for e in E:
                self.add_edge(e)
    
    def add_vertex(self, v):
        self.V.add(v)

    def add_edge(self, e):
        u, v = e
        if u in self.nbrs:
            self.nbrs[u].append(v)
        else:
            self.nbrs[u] = [v]
        if v in self.nbrs:
            self.nbrs[v].append(u)
        else:
            self.nbrs[v] = [u]
    
    def __iter__(self):
        return iter(self.V)
    
    def neighbors(self, v):
        return self.nbrs[v]