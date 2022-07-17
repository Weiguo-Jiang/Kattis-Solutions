N, P = list(map(int, input().split()))
if P == 100:
	print("impossible")
else:
	scores = list(map(int, input().split()))
	cnt = 0
	s = sum(scores)
	while True:
		s += 100
		cnt += 1
		if s / (N+cnt) >= P:
			break
	print(cnt)