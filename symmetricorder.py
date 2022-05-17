cnt = 1
while True:
	n = int(input())
	if n == 0:
		break

	print("SET " + str(cnt))
	l = list()
	for i in range(n):
		name = input()
		l.append(name)

	if n % 2 == 1:
		for i in range(0, n, 2):
			print(l[i])
		for i in range(n-2, -1, -2):
			print(l[i])
	else:
		for i in range(0, n, 2):
			print(l[i])
		for i in range(n-1, -1, -2):
			print(l[i])

	cnt += 1
