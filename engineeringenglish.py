s = set()
while True:
	try:
		line = input().split()
	except EOFError:
		break
	l = list()
	for i in line:
		if i.lower() not in s:
			s.add(i.lower())
			l.append(i)
		else:
			l.append('.')
	print(" ".join(l))