vowels = ['a', 'e', 'i', 'o', 'u', 'y']
while True:
	try:
		inp = input().split()
	except EOFError:
		break
	l = list()
	for i in inp:
		if i[0] in vowels:
			l.append(i+"yay")
			continue
		for j in range(len(i)):
			if i[j] in vowels:
				l.append(i[j:]+i[0:j]+"ay")
				break
	print(" ".join(l))