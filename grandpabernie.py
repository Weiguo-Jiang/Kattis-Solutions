n = int(input())
d = dict()
for i in range(n):
	s, y = input().split()
	y = int(y)
	if s in d:
		d[s].append(y)
	else:
		d[s] = [y]

for key, value in d.items():
	value.sort()

q = int(input())
for i in range(q):
	s, k = input().split()
	k = int(k)
	print(d[s][k-1])