d = dict()
while True:
	inp = input().split()
	if inp == ['0']:
		break

	if '=' in inp:
		d[inp[0]] = int(inp[2])
	else:
		l = [i for i in inp if i != '+']
		undefined = list()
		s = 0
		for i in range(len(l)):
			if l[i] in d:
				s += d[l[i]]
			elif l[i].isdigit():
				s += int(l[i])
			else:
				undefined.append(l[i])
		
		if s == 0:
			print(" + ".join(undefined))
		elif len(undefined) == 0:
			print(s)
		else:
			print(s, end=" + ")
			print(" + ".join(undefined))
		