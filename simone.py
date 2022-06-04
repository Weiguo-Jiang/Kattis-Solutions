N, K = list(map(int, input().split()))
d = dict()
inp = list(map(int, input().split()))
for i in inp:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1

for i in range(1, K+1):
	if i not in d:
		d[i] = 0

m = 1001
for key, value in d.items():
	if value < m:
		m = value

l = list()
for key, value in d.items():
	if value == m:
		l.append(key)

l.sort()
print(len(l))
l = [str(i) for i in l]
print(" ".join(l))