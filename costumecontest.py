minCnt = 1001
N = int(input())
d = dict()
for i in range(N):
	cos = input()
	if cos in d:
		d[cos] += 1
	else:
		d[cos] = 1

for key, value in d.items():
	if value < minCnt:
		minCnt = value

l = list()
for key, value in d.items():
	if value == minCnt:
		l.append(key)

for i in sorted(l):
	print(i)