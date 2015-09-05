#inplace sort
from random import randint
def quicksort(a,start,end):
	if start<end:
		p=selectpivot(start,end)
		if p != start:
            a[p], a[start] = a[start], a[p]
		newi=partition(a,start,end)
		quicksort(a,start,newi-1)
		quicksort(a,newi+1,end)

def partition(a,s,e):
	pivot =a[s]
	i=s+1
	for j in xrange(s+1,e+1):
		if(a[j]<pivot):
			a[i],a[j]=a[j],a[i]
			i+=1
	a[i-1],a[s]=a[s],a[i-1]
	return i-1

def selectpivot(s, e):
    return randint(s,e)

arr=[2,5,7,3,8,1,4,6]
quicksort(arr,0,len(arr)-1)