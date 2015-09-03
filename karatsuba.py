def karatsuba(x,y):
	if x<100 or y<100:
		return x * y
	base=10
	n=base**min(len(str(x))/2,len(str(y))/2)
	a,b,c,d=x/n,x%n,y/n,y%n
	z0=karatsuba(a,c)
	z1=karatsuba(b,d)
	z2=karatsuba((a+b),(c+d))-z0-z1
	return ((n**2)*z0)+(n*z2)+z1


# prriint karatsuba(5678,1234)

	
