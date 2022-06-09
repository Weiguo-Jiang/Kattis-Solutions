b, c, d, l = list(map(int, input().split()))
ll = list()
for i in range(l//b+1):
	l -= i*b
	if l == 0:
		ll.append([str(i), '0', '0'])
		l += i*b
		continue
	for j in range(l//c+1):
		l -= j*c
		if l == 0:
			ll.append([str(i), str(j), '0'])
			l += j*c
			continue
		for k in range(l//d+1):
			l -= k*d
			if l == 0:
				ll.append([str(i), str(j), str(k)])
				l += k*d
				continue
			l += k*d
		l += j*c
	l += i*b
if len(ll) == 0:
	print("impossible")
else:
	for i in ll:
		print(" ".join(i))