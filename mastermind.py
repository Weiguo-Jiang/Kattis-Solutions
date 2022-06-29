n, c, g = input().split()
n = int(n)
r = 0
for i in range(n):
	if c[i] == g[i]:
		r += 1

d1 = dict()
d2 = dict()
for i in range(n):
	if c[i] in d1:
		d1[c[i]] += 1
	else:
		d1[c[i]] = 1

	if g[i] in d2:
		d2[g[i]] += 1
	else:
		d2[g[i]] = 1

cnt = 0
for key, value in d1.items():
	if key in d2:
		cnt += min(value, d2[key])
s = cnt-r

print(r, s)