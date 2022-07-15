while True:
	n = int(input())
	if n == 0:
		break
	l = [-1 for i in range(32)]
	for i in range(n):
		inp = input().split()
		command = inp[0]

		if command == 'SET':
			l[int(inp[1])] = 1
		elif command == 'CLEAR':
			l[int(inp[1])] = 0
		elif command == 'AND':
			b1, b2 = int(inp[1]), int(inp[2])
			if l[b1] == 0 or l[b2] == 0:
				l[b1] = 0
			elif l[b1] == -1 or l[b2] == -1:
				l[b1] = -1
		elif command == 'OR':
			b1, b2 = int(inp[1]), int(inp[2])
			if l[b1] == 1 or l[b2] == 1:
				l[b1] = 1
			elif l[b1] == -1 or l[b2] == -1:
				l[b1] = -1
	l.reverse()
	ll = list()
	for i in l:
		if i == -1:
			ll.append('?')
		else:
			ll.append(str(i))
	print("".join(ll))