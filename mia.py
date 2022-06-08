d = dict()
d['12'] = 100
d['21'] = 100
d['66'] = 99
d['55'] = 98
d['44'] = 97
d['33'] = 96
d['22'] = 95
d['11'] = 94
for i in range(11, 67):
	if str(i) not in d:
		d[str(i)] = i

while True:
	inp = input()
	if inp == "0 0 0 0":
		break
	s0, s1, r0, r1 = inp.split()
	p1 = max(d[s0+s1], d[s1+s0])
	p2 = max(d[r0+r1], d[r1+r0])
	if p1 > p2:
		print("Player 1 wins.")
	elif p2 > p1:
		print("Player 2 wins.")
	else:
		print("Tie.")