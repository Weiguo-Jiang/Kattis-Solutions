while True:
	try:
		a, b, c = list(map(int, input().split()))
	except EOFError:
		break

	l = list()
	l.append('0.')
	for i in range(c):
		a *= 10
		if a < b:
			l.append('0')
		else:
			l.append(str(a//b))
			a %= b
	print("".join(l))