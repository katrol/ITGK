def streng_sjekk(streng1, streng2):
	i = 0
	if(len(streng1) == len(streng2)):
		while(i < len(streng1)):
			if streng1[i] != streng2[i]:
				return False
			i += 1
		return True
	else:
		return False

def streng_revers(streng):
	streng2 = ''
	for i in range(len(streng)):
		streng2 += streng[(i + 1) * (-1)]
	return(streng2)

def palindrom(streng):
	for i in range(len(streng) // 2):
		if(streng[i] != streng[(i + 1) * (-1)]):
			return(False)
	return(True)

def streng_func(streng1, streng2):
	if streng2 in streng1:
		return(streng1.find(streng2))
	else:
		return(False)

