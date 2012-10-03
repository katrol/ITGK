antall_kvinner = 0
antall_menn = 0
antall_sosmedier = 0
antall_facebook = 0
antall_timer_sosmedier = 0
fortsett = True
print('Du kan til en hver tid skrive "hade" for å avslutte')

while fortsett:
	kjonn = input('Skriv "k" om du er kvinne og "m" om du er mann: ')
	if kjonn != 'hade':
		if kjonn == 'k':
			antall_kvinner += 1
		if kjonn == 'm':
			antall_menn += 1
		alder = input('Hvor gammel er du?')
		if alder != 'hade':
			alder = int(alder)
			if(alder > 15 and alder < 26):
				aktiv_sosmedier = input('Benytter du deg av ett eller flere sosiale medier? (svar ja eller nei)')
				if aktiv_sosmedier != 'hade':
					if aktiv_sosmedier == 'ja':
						antall_sosmedier += 1
						if kjonn == 'k':
							medlem_facebook = input('Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse?' )
						elif kjonn == 'm':
							medlem_facebook = input('Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse?' )
						if medlem_facebook != 'hade':
							if medlem_facebook == 'ja':
								antall_facebook += 1
							timer_sosmedier = input('Hvor mange timer bruker du i snitt daglig på sosiale medier?' )
							if timer_sosmedier != 'hade':
								timer_sosmedier = int(timer_sosmedier)
								antall_timer_sosmedier += timer_sosmedier
							else:
								fortsett = False
						else:
							fortsett = False
				else:
					fortsett = False
			else:
				print('Du er i feil aldersgruppe')
		else:
			fortsett = False
	else:
		fortsett = False
print('Antall kvinner: ', antall_kvinner, '\nAntall menn: ', antall_menn, '\nAntall som bruker sosiale medier: ', antall_sosmedier, '\nAntall som bruker facebook: ', antall_facebook, '\nAntall timer de tilsammen bruker på sosiale medier: ', antall_timer_sosmedier)
