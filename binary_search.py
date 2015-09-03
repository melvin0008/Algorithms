from mergesort import mergesort

def binary_search(a,s):
	a=mergesort(a)
	n=len(a)
	if n>0:
		mid=a[n/2]
		if mid ==s:
			return True
		elif s < mid:
			return binary_search(a[:n/2],s)
		elif s> mid:
			return binary_search(a[(n/2)+1:],s)
	return False

# binary_search([5,20,1,8,25,80,15],18)


