from collections import deque

C, P, X, L = list(map(int, input().split()))
if X == L:
	print("leave")
else:
	d = dict()
	for i in range(C):
		d[i] = set()
	for i in range(P):
		c1, c2 = list(map(int, input().split()))
		c1 -= 1
		c2 -= 1
		d[c1].add(c2)
		d[c2].add(c1)
	half = list()
	for i in range(C):
		half.append(len(d[i])//2)

	q = deque()
	q.append(L-1)
	visited = set()
	visited.add(L-1)

	while q:
		p = q.popleft()
		for partner in d[p]:
			d[partner].remove(p)
			if partner not in visited and len(d[partner]) <= half[partner]:
				q.append(partner)
				visited.add(partner)
		del d[p]
	
	if X-1 in d:
		print("stay")
	else:
		print("leave")
