N, C = list(map(int, input().split()))
inp = list(map(int, input().split()))
maxCnt = 0
for i in range(N):
	c = 0
	cnt = 0
	for j in range(i, N):
		if c+inp[j] <= C:
			c += inp[j]
			cnt += 1
	if cnt > maxCnt:
		maxCnt = cnt
print(maxCnt)
