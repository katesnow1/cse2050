class Graph:
    def is_connected(self, u, v):
        """Returns true if u is connected to v"""
        return self._is_connected(u, v, visited=set())
    
    def _is_connected(self, u, v, visited):
        """Returns true if u is connected to v"""
        # Memoization
        if u in visited: return False
        else: visited.add(u)

        # Recursive solution
        # Base Case
        if u == v: return True

        # Recursive Case
        return any(self._is_connected(n, v, visited) for n in self.neighbors(u))
    
    def dfs(self, source):
        """Depth-first search starting at v"""
        tree = {source:None} # initialize tree None -> source -> ? ->?
                        #                              +--> ? ->
        self._dfs(source, tree) # None
        return tree
    
    def _dfs(self, v, tree):
        """Depth-first search starting at v"""
        for n in self.neighbors(v):
            if n not in tree:
                tree[n] = v # None -> source -> ... -> v -> n
                self._dfs(n, tree)