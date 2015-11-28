from collections import defaultdict
def twoelem(A,K):
	d=defaultdict()
	for val in A:
		d[val]=1
	for val in A:
		if K-val in d:
			return val,K-val

def twoelementsclose(A,K):
	n=len(A)
	A.sort()
	m=float('inf')
	minl,minr=0,n-1,
	minx=A[1]
	i,j=0,n-1
	for x in A:
		while i<j:
			s=A[i]+A[j]+x
			if abs(s-K) < abs(m):
				m=s-K
				minl=i
				minr=j
				minx=x	
			if(s==K):
				minl=i
				minr=j
				minx=x
				break
			elif(s<K):
				i+=1
			else:
				j-=1
	return minx,A[minl],A[minr]

print twoelementsclose([1,60,-10,70,-80,85],63)	
#print twoelem([1,4,45,6,10,-8],11)
