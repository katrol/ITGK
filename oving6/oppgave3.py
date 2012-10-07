from math import *

def vektor(x,y,z):
	return [x,y,z]

def skriv_ut(vektor):
	print('Vektoren er (', vektor[0],',', vektor[1],',', vektor[2],')', sep='')

def skalarmult(vektor, skalar):
	for i in range(3):
		vektor[i] = vektor[i] * skalar
	return(vektor)

def vektor_lengde(vektor):
	return(sqrt(vektor[0]**2 + vektor[1]**2 + vektor[2]**2))

def indreprodukt(vektor1,vektor2):
	produkt = 0
	for i in range(3):
		produkt += vektor1[i] * vektor2[i]
	return(produkt)

vec1 = vektor(1,2,3)
skriv_ut(vec1)


skalar1 = int(input('Skriv inn et heltall å multiplisere med: '))

lengde1 = vektor_lengde(vec1)
print('Lengden før er', lengde1)

vec1 = skalarmult(vec1, skalar1)
skriv_ut(vec1)

lengde2 = vektor_lengde(vec1)
print('Lengden etter er', lengde2)

print('Forholdet mellom lengdene er', lengde1/lengde2)

vec2 = vektor(5,3,1)

print('Produktet av vektorene er', indreprodukt(vec1,vec2))

