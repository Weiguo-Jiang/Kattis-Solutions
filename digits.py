while True:
	x = input()
	if x == 'END':
		break

	l = len(x)
	if l == 1 and int(x) == 1:
		print(1)
	else:
		cnt = 2
		while True:
			cur = len(str(l))
			if cur == l:
				break
			else:
				cnt += 1
				l = cur
		print(cnt)
