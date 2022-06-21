n, m = list(map(int, input().split()))
d = dict()
for i in range(n):
	rule = input().split(' -> ')
	if rule[0] not in d:
		d[rule[0]] = rule[1]

s = input()
for i in range(m):
	l = list()
	for j in s:
		if j in d:
			l.append(d[j])
		else:
			l.append(j)
	s = "".join(l)
print(s)