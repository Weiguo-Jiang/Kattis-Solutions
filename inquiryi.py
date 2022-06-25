n = int(input())
l = list()
s1 = 0
for i in range(n):
	a = int(input())
	l.append(a)
	s1 += a

m = -1
s2 = 0
for i in range(n):
	s2 += l[i]**2
	s1 -= l[i]
	s = s1*s2
	if s > m:
		m = s
print(m)