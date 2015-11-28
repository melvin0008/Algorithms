import heapq

heap=[]
heapq.heappush(heap,(9))
heapq.heappush(heap,(2))
heapq.heappush(heap,(5))
heapq.heappush(heap,(3))
heapq.heappush(heap,(4))

for x in heap:
	print x


heap2=[4,3,9,5,-2,10]
heapq.heapify(heap2)
print heap2[0]
