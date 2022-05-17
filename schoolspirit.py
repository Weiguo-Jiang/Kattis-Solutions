def score(l):
	return sum([0.2*l[i]*((0.8)**i) for i in range(len(l))])

l = list()
n = int(input())
for i in range(n):
	l.append(int(input()))
print(score(l))

cnt = 0
s = 0
for i in range(n):
	ll = l[:i] + l[i+1:]
	d = score(ll)
	s += d
	cnt += 1
print(s/cnt)
