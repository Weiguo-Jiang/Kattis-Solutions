while True:
	try:
		s = input()
	except EOFError:
		break

	degree = 0
	for i in range(len(s)-1, 0, -1):
		d = dict()
		for j in range(0, len(s)-i+1):
			substr = s[j:j+i]
			if substr in d:
				d[substr] += 1
			else:
				d[substr] = 1
		flag = 1
		for key, value in d.items():
			if value < 2:
				flag = 0
				break
		if flag:
			degree = i
			break
	print(degree)