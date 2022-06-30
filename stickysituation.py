N = int(input())
sticks = sorted(list(map(int, input().split())))
flag = 1
for i in range(N-2):
	if sticks[i] + sticks[i+1] > sticks[i+2]:
		print("possible")
		flag = 0
		break
if flag:
	print("impossible")