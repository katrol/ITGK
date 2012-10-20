from math import *
def polynom(x):
	return(x**5 - 4*x**3 + 10*x**2 - 10)

def polynom_derivative(x):
	return(5*x**4 - 12*x**2 + 20*x)
def newton(func, deriv, start, threshold, max_iterations):
	svar = start
	i = 0
	while i < max_iterations:
		svar = svar - func(svar) / deriv(svar)
		if (func(svar) <= threshold and func(svar) >= threshold*(-1)):
			return svar
		i += 1

	return False
print(newton(polynom,polynom_derivative,0.01,0.001,20))
