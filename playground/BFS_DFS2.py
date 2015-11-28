from collections import deque

def BFS(graph,s):
	explored=[s]
	q=deque([s])
	while q:
		vertex=q.popleft()
		for node in graph.getNeighbours(vertex):
			if node not in explored:	
				explored.append(node)
				q.append(vertex)


def DFS(graph,s)
	explored=set([])
	depth_first_search(graph,explored)
	return explored

def depth_first_search(graph,s,explored):
	if s not in explored:
		explored.add(s)
	else:
		return false
	for node in graph.getNeighbours(s):
		if node not in explored:
			depth_first_search(graph,node,explored)
			
		
