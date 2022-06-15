n = int(input())
for i in range(n):
	s = 0
	pw = 0
	inp = input()
	for j in inp:
		if j == ',':
			pw += 1
	l = list()
	for ip in inp.split(','):
		if ip == '':
			l.append(0)
		else:
			l.append(int(ip))
	for k in l:
		s += k*(60**pw)
		pw -= 1
	print(s)