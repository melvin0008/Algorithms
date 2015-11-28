from collections import Counter
import operator
x=[1,2,3,5,4,7,8,6,3,1,2,4,4]
y="melvinphilips"
maxfreq=Counter(x)
ymax=Counter(y)
m=float('-inf')
mk=""
for k,v in maxfreq.iteritems():
	if v>m:
		m,mk=v,k

print mk
	
print max(maxfreq.iteritems(),key=operator.itemgetter(1))[0]	

print max(maxfreq.keys(),key=lambda x : maxfreq[x])

print max(ymax.keys(),key=lambda x: ymax[x]) 
