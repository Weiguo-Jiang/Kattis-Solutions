N = int(input())
Yscore = 0
Nscore = 0
YMaxLead = 0
NMaxLead = 0
maxLead = 0
winByLead = ''

Ystreak = 0
Nstreak = 0
YMaxStreak = 0
NMaxStreak = 0
winByStreak = ''
for i in range(N):
	name = input()
	if name == 'Yraglac':
		Yscore += 1

		Ystreak += 1
		if Ystreak > YMaxStreak:
			YMaxStreak = Ystreak
		Nstreak = 0
	else:
		Nscore += 1

		Nstreak += 1
		if Nstreak > NMaxStreak:
			NMaxStreak = Nstreak
		Ystreak = 0

	if Yscore > Nscore:
		if Yscore - Nscore > YMaxLead:
			YMaxLead = Yscore - Nscore
	elif Yscore < Nscore:
		if Nscore - Yscore > NMaxLead:
			NMaxLead = Nscore - Yscore

if YMaxLead == NMaxLead:
	winByLead = 'Tie'
elif YMaxLead > NMaxLead:
	winByLead = 'Yraglac'
else:
	winByLead = 'Notnomde'

if NMaxStreak == YMaxStreak:
	winByStreak = 'Tie'
elif YMaxStreak > NMaxStreak:
	winByStreak = 'Yraglac'
else:
	winByStreak = 'Notnomde'

if winByLead == winByStreak:
	print("Agree")
else:
	print("Disagree")
