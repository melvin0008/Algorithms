def countinversions(a):
	l=len(a)
	if l <= 1:
		return a,0
	h1,c1=countinversions(a[:l/2])
	h2,c2=countinversions(a[l/2:])
	return merge_count(h1,h2,c1+c2)

def merge_count(h1,h2,count):
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
			count+=len(h1[i:])
	if i< len(h1):
		r.extend(h1[i:])
	else:
		r.extend(h2[j:])
	return r,count	

print countinversions([2,14,1,6,4,70,3])