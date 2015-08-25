def mergesort(a):
	l=len(a)
	if l <= 1:
		return a
	h1=mergesort(a[:l/2])
	h2=mergesort(a[l/2:])
	return merge(h1,h2)

def merge(h1,h2):
	r=[]
	while len(h1) > 0 and len(h2) >0:
		if h1[0] < h2[0]:
			r.append(h1.pop(0))
		else:
			r.append(h2.pop(0))
	if len(h1)>0:
		r.extend(h1)
	else:
		r.extend(h2)
	return r

print mergesort([8,1,3,5,4,50,42,2])