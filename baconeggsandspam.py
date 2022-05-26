while True:
	d = dict()
	n = int(input())
	if n == 0:
		break
	for i in range(n):
		l = input().split()
		name = l[0]
		for j in range(1, len(l)):
			if l[j] not in d:
				d[l[j]] = list()
				d[l[j]].append(name)
			else:
				d[l[j]].append(name)

	keys = sorted([key for key in d])
	for key in keys:
		print(key, end=" ")
		names = sorted(d[key])
		for i in range(len(names)-1):
			print(names[i], end=" ")
		print(names[-1])
	print()