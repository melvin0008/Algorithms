def mergesort(a):
	l=len(a)
	if l <= 1:
		return a
	h1=mergesort(a[:l/2])
	h2=mergesort(a[l/2:])
	return merge2(h1,h2)

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

def merge2(h1,h2):
	i=0
	j=0
	r=[]
	while i<len(h1) and j<len(h2):
		if h1[i] < h2[j]:
			r.append(h1[i])
			i+=1
		else:
			r.append(h2[j])
			j+=1
	if i< len(h1):
		r.extend(h1[i:])
	else:
		r.extend(h2[j:])
	return r	

print mergesort([2,14,1,6,4,70,3])