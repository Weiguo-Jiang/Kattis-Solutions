n = int(input())
for i in range(n):
	inp = input()
	l = list()
	flag = 1
	for j in inp:
		if j == '$':
			l.append('$')
		elif j == '|':
			l.append('|')
		elif j == '*':
			l.append('*')
		elif j == 't':
			if len(l) == 0 or l[-1] != '|':
				print("NO")
				flag = 0
				break
			else:
				l.pop()
		elif j == 'j':
			if len(l) == 0 or l[-1] != '*':
				print("NO")
				flag = 0
				break
			else:
				l.pop()
		elif j == 'b':
			if len(l) == 0 or l[-1] != '$':
				print("NO")
				flag = 0
				break
			else:
				l.pop()
	if len(l) != 0 and flag:
		print("NO")
	elif len(l) == 0 and flag:
		print("YES")
