from math import *
def simpson(func,a,b,h):
	dx = (b - a) / h
	ytotal = 0
	for i in range(h):
		if i == 0:
			ytotal += func(a)
		elif i == h - 1:
			ytotal += func(b)
		elif i % 2 == 0:
			ytotal += 2 * func(a + i * dx)
		else:
			ytotal += 4 * func(a + i * dx)

	return(dx * ytotal / 3)

def function(x):
	return(exp(-x**2))

print(simpson(function,0,1,1000))

def simpson_error(func,a,b,error):
	h = 2
	differanse = 1
	forrige_svar = simpson(func,a,b,h)
	while fabs(differanse) > error:
		h += 2
		svar = simpson(func,a,b,h)
		differanse = forrige_svar - svar
		forrige_svar = svar

	return(svar)

print(simpson_error(function, 0,1,0.00000001))
