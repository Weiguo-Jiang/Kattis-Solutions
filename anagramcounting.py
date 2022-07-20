fact = dict()
fact[0] = 1
for i in range(1, 101):
	fact[i] = i*fact[i-1]

while True:
	try:
		inp = input()
	except EOFError:
		break

	d = dict()
	for i in inp:
		if ord(i) in d:
			d[ord(i)] += 1
		else:
			d[ord(i)] = 1

	ans = fact[len(inp)]
	for i in d:
		ans //= fact[d[i]]
	print(ans)
