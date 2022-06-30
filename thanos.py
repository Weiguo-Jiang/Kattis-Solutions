T = int(input())
for i in range(T):
	P, R, F = list(map(int, input().split()))
	if P > F:
		print(0)
		continue
	cnt = 0
	pop = P
	while pop <= F:
		cnt += 1
		pop *= R
	print(cnt)