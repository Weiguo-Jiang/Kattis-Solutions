d = {'B': 1, 'F': 1, 'P': 1, 'V': 1,
	 'C': 2, 'G': 2, 'J': 2, 'K': 2, 'Q': 2, 'S': 2, 'X': 2, 'Z': 2,
	 'D': 3, 'T': 3,
	 'L': 4,
	 'M': 5, 'N': 5,
	 'R': 6}
while True:
	try:
		word = input()
	except EOFError:
		break
	l = list()
	for i in word:
		if i in d:
			l.append(d[i])
		else:
			l.append(-1)
	
	ll = list()
	cur = -1	
	for i in l:
		if i != cur:
			ll.append(i)
		cur = i

	ll = [str(i) for i in ll if i != -1]
	print("".join(ll))