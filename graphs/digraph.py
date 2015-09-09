from graph import Graph

class digraph(graph):
	"""docstring for digraph"""
	def __init__(self, arg):
		self.vertices_list={}
		self.numVertices=0

	def addEdge(self,vertex1,vertex2,weight=0):
		if vertex1 not in self.vertices_list:
			self.addVertex(vertex1)
		if vertex2 not in self.vertices_list:
			self.addVertex(vertex2)
		self.vertices_list[vertex1].addNeighbour(vertex2,weight)
