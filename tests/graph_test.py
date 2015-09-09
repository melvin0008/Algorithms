from graphs.graphs import Graph
import unittest

class test_graph(unittest.TestCase):

	def setUp(self):
		self.graph= Graph()
		self.graph.addVertices(["s", "a", "b", "c", "d", "e"])
		self.graph.addEdges([("s", "a"), ("s", "b"), ("a", "c"), ("c", "e")])
		self.graph.addEdges([("e", "d"), ("d", "b"), ("a", "b"), ("c", "d")])

	def test_initial_setup(self):
		self.assertEqual(self.graph.numberVertices(),6)
		

	# def test_connections

if __name__ == "__main__":
    unittest.main()