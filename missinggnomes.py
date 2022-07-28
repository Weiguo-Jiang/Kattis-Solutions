n, m = list(map(int, input().split()))
s = set()
l = list()
for i in range(m):
	g = int(input())
	s.add(g)
	l.append(g)

if len(l) == n:
	for i in l:
		print(i)
else:
	missing = list()
	for i in range(n, 0, -1):
		if i not in s:
			missing.append(i)

	ll = list()
	index = 0
	while index < m:
		cur = l[index]
		while len(missing) > 0:
			if missing[-1] < cur:
				ll.append(missing[-1])
				missing.pop()
			else:
				break
		ll.append(cur)
		index += 1

	while missing:
		ll.append(missing[-1])
		missing.pop()

	for i in ll:
		print(i)