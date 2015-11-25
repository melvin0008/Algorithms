class Vertex:
	def __init__(self,key):
		self.key=key
		self.connectedNodes={}

	def addNeighbour(self,v2,wt):
		self.connectedNodes[v2]=wt

	def getConnectedNodes(self):
		return self.connectedNodes.keys()


class Graph:
	def __init__(self):
		self.verticesList={}
		self.numVertices=0

	def __iter__(self):
		return iter(self.verticesList.values())

	def addVertices(self,VertexList):
		for v in VertexList:
			self.addVertex(v)

	def addVertex(self,key):
		self.verticesList[key]=Vertex(key)
		self.numVertices+=1

	def addEdge(self,v1,v2,wt):
		if v1 not in self.verticesList:
			self.addVertex(v1)
		if v2 not in self.verticesList:
			self.addVertex(v2)
		self.verticesList[v1].addNeighbour(v2,wt)

	def getConnections(self,v):
		return self.verticesList[v].getConnectedNodes()

	def hasVertex(self,v):
		return v in self.verticesList

	def addEdges(self,edgesList):
		for edge in edgesList:
			try:
				self.addEdge(edge[0],edge[1],edge[2])
			except IndexError:
				self.addEdge(edge[0],edge[1],0)

	def numberVertices(self):
		return self.numVertices

