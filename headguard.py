while True:
	try:
		inp = input()
	except EOFError:
		break

	l = list()
	cnt = 1
	currChar = inp[0]
	for i in range(1, len(inp)):
		if inp[i] == currChar:
			cnt += 1
		else:
			l.append(str(cnt)+currChar)
			currChar = inp[i]
			cnt = 1
	l.append(str(cnt)+currChar)
	print("".join(l))