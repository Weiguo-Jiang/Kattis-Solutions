P, N = list(map(int, input().split()))
s = set()
flag = 0
day = 0
for i in range(N):
	p = input()
	s.add(p)
	if len(s) == P:
		day = i+1
		flag = 1
		break
if flag:
	print(day)
else:
	print("paradox avoided")
