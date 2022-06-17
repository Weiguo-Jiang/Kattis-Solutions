C, n = list(map(int, input().split()))
cnt = 0
flag = 1
for i in range(n):
	a, b, c = list(map(int, input().split()))

	if a > cnt:
		flag = 0
		break
	cnt -= a

	if cnt+b > C:
		flag = 0
		break
	cnt += b

	if c != 0 and cnt != C:
		flag = 0
		break

	if i == n-1 and (b != 0 or c != 0 or cnt != 0):
		flag = 0
		break

if flag:
	print("possible")
else:
	print("impossible")