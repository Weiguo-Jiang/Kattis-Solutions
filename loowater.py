while True:
	n, m = list(map(int, input().split()))
	if n == 0 and m == 0:
		break

	l = list()
	for i in range(n):
		l.append(int(input()))

	ll = list()
	for i in range(m):
		ll.append(int(input()))

	if n > m:
		print("Loowater is doomed!")
	else:
		l.sort()
		ll.sort()

		cost = 0
		index1 = 0
		index2 = 0
		cnt = 0

		while index2 < m and index1 < n:
			if l[index1] <= ll[index2]:
				cost += ll[index2]
				cnt += 1
				index1 += 1
			index2 += 1
		
		if cnt != n:
			print("Loowater is doomed!")
		else:
			print(cost)
