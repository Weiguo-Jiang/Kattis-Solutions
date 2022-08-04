T = int(input())
for i in range(T):
	n = int(input())
	d = dict()
	for j in range(n):
		inp = input().split(": ")
		c = inp[1].split()
		c.pop()
		c = c[0].split('-')
		c.reverse()

		while len(c) < 10:
			c.append('middle')

		l = list()
		for k in c:
			if k == 'upper':
				l.append('1')
			elif k == 'middle':
				l.append('2')
			else:
				l.append('3')

		classes = "".join(l)
		if classes in d:
			d[classes].append(inp[0])
		else:
			d[classes] = [inp[0]]

	for j in sorted(d):
		for k in sorted(d[j]):
			print(k)
	print("="*30)
