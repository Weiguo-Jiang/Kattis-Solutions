P = int(input())
for i in range(P):
	cnt = 0
	l = list(map(int, input().split()))
	for j in range(1, 11):
		for k in range(1, len(l)-j):
			if max(l[k-1], l[k+j]) < min(l[k:k+j]):
				cnt += 1
	print(l[0], end=" ")
	print(cnt)
