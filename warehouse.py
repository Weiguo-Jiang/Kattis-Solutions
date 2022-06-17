T = int(input())
for i in range(T):
	N = int(input())
	d = dict()
	l = list()
	for j in range(N):
		name, cnt = input().split()
		cnt = int(cnt)
		if name in d:
			d[name] += cnt
		else:
			d[name] = cnt
	for key, value in d.items():
		if value not in l:
			l.append(value)

	l = sorted(l)
	l.reverse()

	print(len(d))

	for j in l:
		ll = list()
		for key, value in d.items():
			if value == j:
				ll.append(key)
		ll = sorted(ll)
		for k in ll:
			print(k + " " + str(j))
