from collections import deque
from graphs import Graph

def BFS(graph,s):
	if not graph.hasVertex(s):
		raise Exception("Node %s not in graph" % s)
	explored=set([s])
	q=deque([s])
	while len(q)!=0:
		vertex= q.popleft()
		for neighbour in graph.getNeighbours(vertex):
			if neighbour not in explored:
				explored.add(neighbour)
				q.append(neighbour)
	return explored