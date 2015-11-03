from collections import deque

def BFS(gr,s):
	explored=[s]
	q=deque([s])
	while len(q)!=0:
		vertex=q.popleft()
		for v in gr.getConnections(vertex):
			if v not in explored:
				explored.append(v)
				q.append(v)
	return explored

def TopologicalHelper(gr,s,explored,c):
	current_label=c
	def DFS(gr,s,explored,current_label):
		print current_label
		if s not in explored:
			explored.append(s)
		else:
			return explored
		for v in gr.getConnections(s):
			if v not in explored:
				DFS(gr,v,explored,current_label)
				print str(current_label)+v
				current_label-=1
		return explored
	DFS(gr,s,explored,current_label)

def DFS_loop(gr,s):
	current_label=6
	explored=[]
	TopologicalHelper(gr,s,explored,current_label)
	return explored
