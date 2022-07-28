from collections import deque

N, M = list(map(int, input().split()))
d = dict()
for i in range(M):
	a, b = list(map(int, input().split()))
	if a in d:
		d[a].append(b)
	else:
		d[a] = [b]

	if b in d:
		d[b].append(a)
	else:
		d[b] = [a]

visited = set()
visited.add(1)
q = deque()
q.append(1)
while q:
	h = q.popleft()
	if h in d:
		for neighbour in d[h]:
			if neighbour not in visited:
				visited.add(neighbour)
				q.append(neighbour)

if len(visited) == N:
	print("Connected")
else:
	for i in range(1, N+1):
		if i not in visited:
			print(i)