from collections import deque

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

def DFS(graph,s):
	explored=set([])
	depth_first_search(graph,s,explored)
	return explored

def depth_first_search(graph,s,explored):
	if s not in explored:
		explored.add(s)
	else:
		return False
	for neighbour in graph.getNeighbours(s):
		if neighbour not in explored:
			depth_first_search(graph,neighbour,explored)