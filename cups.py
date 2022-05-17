n = int(input())
d = dict()
l = list()
for i in range(n):
	a, b = input().split()
	try:
		a = int(a)
	except ValueError:
		b = int(b)
		d[b] = a
		l.append(b)
		continue

	d[a/2] = b
	l.append(a/2)

l = sorted(l)
for i in l:
	print(d[i])