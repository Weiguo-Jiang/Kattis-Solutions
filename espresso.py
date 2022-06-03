n, s = list(map(int, input().split()))
cap = s
cnt = 0
for i in range(n):
	inp = input()
	if inp[-1] == 'L':
		l = int(inp[0]) + 1
		if cap >= l:
			cap -= l
		else:
			cap = s
			cap -= l
			cnt += 1
	else:
		l = int(inp)
		if cap >= l:
			cap -= l
		else:
			cap = s
			cap -= l
			cnt += 1
print(cnt)