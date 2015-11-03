from graph import Graph
from BFS_DFS import *
import unittest

class test_graph(unittest.TestCase):

	def setUp(self):
		self.graph= Graph()
		self.graph.addVertices(["s", "a", "b", "c", "d", "e"])
		self.graph.addEdges([("s", "a"), ("s", "b"), ("a", "c"), ("c", "e"),("b", "d")])

	def test_initial_setup(self):
		self.assertEqual(self.graph.numberVertices(),6)

	def test_bfs_undirected_graph(self):
		self.assertEqual(BFS(self.graph, "s"), ["s", "a", "b", "c", "d", "e"])

	def test_dfs_undirected_graph(self):
		self.assertEqual(DFS_loop(self.graph, "s"), ["s", "a", "c", "e", "b", "d"])

if __name__ == "__main__":
    unittest.main()