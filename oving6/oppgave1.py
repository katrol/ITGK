n = int(input('Skriv inn et heltall: '))
i = 1
summ = 0

while (summ + i**2) <= n:
	summ += i**2
	i += 1

print('Summen ble', summ, 'og', i, 'kvadrattall ble lagt sammen.')
