T = int(input())
for i in range(T):
	blank = input()
	N = int(input())
	cnt = 0
	for j in range(N):
		cnt += int(input())
	if cnt % N == 0:
		print("YES")
	else:
		print("NO")