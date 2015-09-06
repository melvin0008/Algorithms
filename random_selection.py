from random import randint

def randomselection(a,l,i):
	if len(a)<=1:
		return a[0]
	p=selectpivot(0,l)
	if p != 0:
		a[p], a[0] = a[0], a[p]
	j=partition(a,0,l)
	if j==i:
		return a[j]
	if j> i:
		return randomselection(a[:j],len(a[:j])-1,i)
	else:
		return randomselection(a[j+1:],l-j-1,i-j-1)

def partition(a,s,e):
	pivot =a[s]
	i=s+1
	for j in xrange(s+1,e+1):
		if(a[j]<=pivot):
			a[i],a[j]=a[j],a[i]
			i+=1
	a[i-1],a[s]=a[s],a[i-1]
	return i-1

def selectpivot(s, e):
    return randint(s,e)

arr=[2,5,7,3,8,1,4,6]
print randomselection(arr,len(arr)-1,2)
