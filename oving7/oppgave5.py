from math import *
def is_prime(tall):
	for i in range(sqrt(tall)):
		if tall % i == 0:
			return False
	return True

def seperate(tall, threshold):
	mindre_tall = []
	store_tall = []
	for i in tall:
		if tall < threshold:
			mindre_tall.append(i)
		else:
			store_tall.append(i)
	return(mindre_tall,store_tall)

def multiplication_table(n):
	table = []
	inner_table = []
	for i in range(n):
		for j in range(n):
			inner_table.append((j + 1) * (i + 1))
		table.append(inner_table)
		inner_table = []
	
	return(table)

print(multiplication_table(3))
