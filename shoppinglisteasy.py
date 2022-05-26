n, m = list(map(int, input().split()))
d = dict()
for i in range(n):
	l = input().split()
	for j in l:
		if j in d:
			d[j] += 1
		else:
			d[j] = 1
cnt = 0
l = list()
for key, value in d.items():
	if value == n:
		cnt += 1
		l.append(key)
print(cnt)
for i in sorted(l):
	print(i)