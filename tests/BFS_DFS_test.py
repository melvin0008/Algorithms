import unittest
from graphs.graphs import Graph
from graphs.BFS_DFS import *

class BFS_test(unittest.TestCase):
	def setUp(self):
		self.graph= Graph()
		self.graph.addVertices(["s", "a", "b", "c", "d", "e"])
		self.graph.addEdges([("s", "a"), ("s", "b"), ("a", "c"), ("c", "e")])
		self.graph.addEdges([("e", "d"), ("d", "b"), ("a", "b"), ("c", "d")])
		self.graph.addEdges([("g", "h"), ("f", "g")])
		self.graph.addEdges([("j", "k"), ("j", "l")])

	def test_BFS_method(self):
		self.assertEqual(len(BFS(self.graph,"s")),6)
		self.assertEqual(len(BFS(self.graph,"j")),3)
		self.assertEqual(len(BFS(self.graph,"g")),3)

	def test_DFS_method(self):
		self.assertEqual(len(DFS(self.graph,"s")),6)
		self.assertEqual(len(DFS(self.graph,"j")),3)
		self.assertEqual(len(DFS(self.graph,"g")),3)

if __name__ == "__main__":
    unittest.main()
