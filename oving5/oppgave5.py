def fib1(n):
	fib = 1
	fibmin1 = 0
	fibmin2 = 0
	for i in range(2,n + 1):
		fibmin2 = fibmin1
		fibmin1 = fib
		fib = fibmin1 + fibmin2
	print(fib)

fib1(6)	

def fib2(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return(fib2(n-1) + fib2(n-2))

print(fib2(7))


def listefib(n):
	fibliste = []
	for i in range(n):
		fibliste.append(fib2(i))
	print(fibliste)

listefib(10)
