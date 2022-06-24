def found(d, c1, c2):
	# BFS
	visited = set()
	queue = list()
	queue.append(c1)

	while len(queue) != 0:
		c = queue.pop(0)

		if c in d:
			for i in d[c]:
				if i not in visited:
					visited.add(i)
					queue.append(i)

	if c2 in visited:
		return 1
	else:
		return 0


m, n = list(map(int, input().split()))
d = dict()
for i in range(m):
	a, b = input().split()
	if a not in d:
		d[a] = [b]
	else:
		d[a].append(b)

for i in range(n):
	flag = 1
	ori, trans = input().split()
	if len(ori) != len(trans):
		print("no")
		continue
	for j in range(len(ori)):
		if ori[j] != trans[j]:
			if not found(d, ori[j], trans[j]):
				flag = 0

	if flag:
		print("yes")
	else:
		print("no")