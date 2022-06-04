N, T = list(map(int, input().split()))
l = list()
for i in range(N):
	inp = int(input())
	l.append(inp)
l.sort()
l.reverse()

for i in range(N):
	for j in range(i):
		l[j] -= T

flag = 1
for i in l:
	if i <= 0:
		print("NO")
		flag = 0
		break
if flag:
	print("YES")