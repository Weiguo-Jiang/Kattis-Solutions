while True:
	try:
		l = input().split()
	except EOFError:
		break
	s = 0
	cnt = 0
	name = list()
	for i in l:
		if i[0] >= '0' and i[0] <= '9':
			s += float(i)
			cnt += 1
		else:
			name.append(i)
	print(s/cnt, end=" ")
	print(" ".join(name))