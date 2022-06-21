day = 0
d = dict()
d1 = dict()
lll = list()
while True:
	try:
		inp = input()
	except EOFError:
		break

	if inp == 'OPEN':
		day += 1
	elif inp == 'CLOSE':
		ll = list()
		ll.append("Day " + str(day))
		l = list()
		for key, value in d1.items():
			l.append(key)
		l.sort()

		for i in l:
			ll.append(i+" $"+str(round(d1[i], 1))+"0")

		lll.append(ll)
		lll.append('\n')

		d = dict()
		d1 = dict()
	else:
		inp = inp.split()
		if inp[1] not in d1:
			d1[inp[1]] = 0

		if inp[0] == 'ENTER':
			d[inp[1]] = int(inp[2])
		elif inp[0] == 'EXIT':
			d1[inp[1]] += (int(inp[2])-d[inp[1]])*0.10

for i in range(len(lll)-1):
	for j in lll[i]:
		if j == '\n':
			print()
		else:
			print(j)
