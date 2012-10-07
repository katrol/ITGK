teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114, 109, 11, 2, 21, 45, 2, 26, 81, 54, 14, 118, 108, 117, 27, 115, 43, 70, 58, 107]

def mynter(gram):
	tjuere = gram//40
	gram %= 40
	tiere = gram//20
	gram %= 20
	femmere = gram//10
	gram %= 10
	enere = gram//2
	gram %= 2
	orer = gram
	
	return tjuere, tiere, femmere, enere, orer

tjuere = 0
tiere = 0
femmere = 0
enere = 0
orer = 0
for i in teeth:
	tjue, ti, fem, en, ore = mynter(i)
	tjuere += tjue
	tiere += ti
	femmere += fem
	enere += en
	orer += ore

print('Feen trenger', tjuere, '20-kroner,', tiere, '10-kroner,', femmere, '5-kroner,', enere, '1-kroner,', orer, '50-øringer')
