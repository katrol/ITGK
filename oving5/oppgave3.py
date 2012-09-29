def gcd(a,b):
	while(b != 0):
		gammel_b = b
		b = a % b
		a = gammel_b
	return(a)

def reduce_fraction():
	a = int(input('Skriv inn telleren: '))
	b = int(input('Skriv inn nevneren: '))

	divisor = gcd(a,b)
	
	a = a / divisor
	b = b / divisor

	return(a,b)

def main():
	a,b = reduce_fraction()
	print(format(a, '.0f'),'/',format(b, '.0f'), sep='')

main()
