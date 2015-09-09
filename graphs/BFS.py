from collections import deque
from graphs import Graphs

def BFS(graph,s):
	if not graph.hasVertex(s):
		raise Exception("Node %s not in graph" % s)
	explored=set([s])
	q=deque([s])
	while not q:
		vertex= q.popleft()
		for neighbour in graph.getConnections():
			if neighbour not in explored:
				explored.add(neighbour)
				q.append(neighbour)
	return explored