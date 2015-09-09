class Vertex(object):
	def __init__(self,key):
		self.key=key
		self.connected_nodes={}

	def __str__(self):
		return str(self.key) + ' adjacent: ' + str([x for x in self.connected_nodes])

	def getConnections(self):
		return self.connected_nodes.keys()

	def addNeighbour(self,neighbour,weight):
		self.connected_nodes[neighbour]=weight

	def getWeight(self,vertex2):
		return self.connected_nodes[vertex2]


class Graph(object):
	def __init__(self):
		self.vertices_list={}
		self.numVertices=0

	def __iter__(self):
		return iter(self.vertices_list.values())

	def addVertex(self,key):
		self.vertices_list[key]=Vertex(key)
		self.numVertices+=1

	def addVertices(self,vertices):
		for vertex in vertices:
			self.addVertex(vertex)

	def getVertex(self,vertex):
		if vertex in self.vertices_list:
			return self.vertices_list[vertex]
		else:
			return None

	def hasVertex(self,vertex):
		return vertex in vertices_list

	def getVertices(self):
		return self.vertices_list.keys()

	def addEdge(self,vertex1,vertex2,weight=0):
		if vertex1 not in self.vertices_list:
			self.addVertex(vertex1)
		if vertex2 not in self.vertices_list:
			self.addVertex(vertex2)
		self.vertices_list[vertex1].addNeighbour(vertex2,weight)

	def addEdges(self,edgesList):
		for edge in edgesList:
			self.addEdge(edge[0],edge[1],edge[2])

	def getEdges(self):
		edgeList=[]
		for vertex1,vertex2 in self.vertices_list.items():
			print vertex1, vertex2.getConnections()

