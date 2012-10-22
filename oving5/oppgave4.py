def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	return False

def weekday_newyear(year):
	dagtall = -1
	for i in range(1900, year + 1):
		if is_leap_year(i - 1):
			dagtall += 2
		else:
			dagtall += 1
	dagtall %= 7

	if dagtall == 0:
		dag = 'man'
	elif dagtall == 1:
		dag = 'tir'
	elif dagtall == 2:
		dag = 'ons'
	elif dagtall == 3:
		dag = 'tor'
	elif dagtall == 4:
		dag = 'fre'
	elif dagtall == 5:
		dag = 'lor'
	else:
		dag = 'son'
	return(dagtall,dag)

for i in range(1900,1920):
	bla, dag = weekday_newyear(i)
	print(i, dag)

def is_workday(weekday):
	if ((weekday == 5) or (weekday == 6)):

		return False
	else:
		return True

def workdays_in_year(year):
	workdays = 0
	newyear, bla = weekday_newyear(year)
	if is_leap_year(year):
		days = 366
	else:
		days = 365
	for i in range(days):
		if is_workday((newyear + i) % 7):	
			workdays += 1
	return(workdays)

for i in range(1900,1920):
	print(i, 'har', workdays_in_year(i), 'arbeidsdager')
weekday_newyear(2012)
