c = 1
while True:
	try:
		e, m = list(map(int, input().split()))
	except EOFError:
		break
	cnt = 0
	while True:
		if e == 0 and m == 0:
			break
		e += 1
		m += 1
		if e == 365:
			e = 0
		if m == 687:
			m = 0
		cnt += 1
	print("Case " + str(c) + ": ", end="")
	print(cnt)
	c += 1