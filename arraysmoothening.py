N, K = list(map(int, input().split()))
if K == N:
	print(0)
else:
	inp = list(map(int, input().split()))
	d = dict()
	for i in inp:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	if K == 0:
		ans = -1
		for key in d:
			if d[key] > ans:
				ans = d[key]
		print(ans)
	else:

		l = list()
		l.append(0)
		for i in d:
			l.append(d[i])
		l.sort()

		s = 0
		cnt = 1
		for i in range(len(l)-1, 0, -1):
			s += (cnt*(l[i]-l[i-1]))
			if s == K:
				print(0)
				break
			elif s > K:
				s -= (cnt*(l[i]-l[i-1]))
				rem = K-s
				print(l[i]-(rem//cnt))
				break
			cnt += 1