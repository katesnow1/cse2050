from Graph import Graph, EdgeSetGraph, AdjacencySetGraph
import unittest

class GraphTestFactory:
    def setUp(self, graph_type):
        """sets up the type of graph that will be tested"""
        self.graph_type = graph_type

    def test_empty_init(self):
        """Test initializes of an empty graph and adding vertices and edges"""
        g = self.graph_type()
        self.assertEqual(len(g.V), 0)
        g.add_vertex(0)
        self.assertEqual(len(g.V), 1)
        self.assertTrue(0 in g.V)
        g.add_vertex(1)
        self.assertEqual(len(g.V), 2)
        self.assertTrue(1 in g.V)
        g.add_edge((0,1))
        i = 1
        for nbr in g.nbrs(0):
            self.assertEqual(nbr, i)
            i+=1

    def test_params_init(self):
        """Tests initialization of a graph with params"""
        V = {0,1,2,3}
        E = {(1,2), (2,3), (0,1), (1,3)}
        g = self.graph_type(V, E)
        self.assertEqual(len(g.V), 4)
        for i in range(len(V)):
            self.assertTrue(i in g.V)
        for nbr in g.nbrs(0):
            self.assertEqual(nbr, 1)

    def test_is_connected_simple(self):
        """Tests the is_connected method for a simple graph"""
        V = {0,1,2,3,4,5}
        E = {(1,2),(0,1), (1,3), (4,5)}
        g = self.graph_type(V,E)
        self.assertTrue(g.is_connected(0,3))
        self.assertTrue(g.is_connected(4,5))
        self.assertFalse(g.is_connected(4,2))
              

    def test_is_connected_cycle(self):
        """Tests is_connected for a graph with a cycle"""
        V = {0,1,2,3,4,5}
        E = {(1,2), (2,3), (0,1), (1,3), (4,5)}
        g = self.graph_type(V,E)
        self.assertTrue(g.is_connected(0,3))
        self.assertTrue(g.is_connected(4,5))
        self.assertFalse(g.is_connected(4,2))

    def test_bfs(self):
        """Tests breadth first search"""
        V = {'A', 'B','C', 'D', 'E', 'F', 'G', 'H'}
        E = {('A', 'B'), ('A', 'C'), ('A', 'F'), ('B', 'D'), ('B', 'H'),('B', 'G'),('C','F'), ('C', 'D'),('D', 'E'),('E', 'G')}
        dist_from_A_expected = {'A':0, 'B':1, 'C':1, 'D':2, 'E':3, 'F':1, 'G':2, 'H':2}
        tree = self.graph_type(V,E)
        dist_from_A_actual = dict()
        bfs_tree = tree.bfs('A')
        for child in tree:
            dis = 0
            node = child
            while bfs_tree[node] is not None:
                node = bfs_tree[node]
                dis += 1
            dist_from_A_actual[child] = dis
            
        self.assertEqual(dist_from_A_actual, dist_from_A_expected)


    def test_count_trees(self):
        """Tests count_trees method"""
        V = {0,1,2,3,4}
        E = {(0,1),(0,2),(1,2),(3,4)}
        g = self.graph_type(V,E)
        trees, count = g.count_trees()
        tree1 = trees[0]
        tree2 = trees[1]
        self.assertTrue(0 in tree1)
        self.assertTrue(1 in tree1)
        self.assertTrue(2 in tree1)
        self.assertTrue(3 in tree2)
        self.assertTrue(4 in tree2)
        self.assertEqual(count, 2)

    def test_shortest_path(self):
        """Tests shortest_path method"""
        V = {0,1,2,3,4,5}
        E = {(0,1),(0,2),(1,2),(2,3),(3,4),(3,5),(1,4)}
        g = self.graph_type(V,E)
        self.assertEqual(len(g.shortest_path(0,1)), 2)
        self.assertEqual(len(g.shortest_path(0,2)), 2)
        self.assertEqual(len(g.shortest_path(0,3)), 3)
        self.assertEqual(len(g.shortest_path(0,4)), 3)
        self.assertEqual(len(g.shortest_path(0,5)), 4)
        path = g.shortest_path(0,5)
        self.assertTrue(path[1] in g.nbrs(path[0]))
        self.assertTrue(path[2] in g.nbrs(path[1]))
        self.assertTrue(path[3] in g.nbrs(path[2]))



class TestAdjacency(GraphTestFactory, unittest.TestCase):
    
    def setUp(self):
        """Sets up the edjacency set graph tests"""
        super().setUp(AdjacencySetGraph)

class TestEdge(GraphTestFactory, unittest.TestCase):
    
    def setUp(self):
        """sets up the edge set graph tests"""
        super().setUp(EdgeSetGraph)

class TestInitError(unittest.TestCase):

    def test_init_error(self):
        with self.assertRaises(NotImplementedError):
            g = Graph()



if __name__ == '__main__':
    unittest.main()