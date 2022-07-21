P = int(input())
for i in range(P):
	K, N = list(map(int, input().split()))
	c = N
	l = list()
	while N != 0:
		inp = list(map(int, input().split()))
		for j in inp:
			l.append(j)
		N -= len(inp)

	ll = sorted(l)
	cnt = 0
	for j in range(c):
		if l[j] == ll[cnt]:
			cnt += 1
	print(K, end=" ")
	print(c-cnt)