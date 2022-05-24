n = int(input())
d = dict()
m = -1
for i in range(n):
	l = list(map(int, input().split()))
	l = " ".join([str(i) for i in sorted(l)])
	if l in d:
		d[l] += 1
	else:
		d[l] = 1
	if d[l] > m:
		m = d[l]

o = 0
for key, value in d.items():
	if value == m:
		o += m
print(o)
