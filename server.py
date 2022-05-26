n, T = list(map(int, input().split()))
l = [int(i) for i in input().split()]
s = 0
cnt = 0
for i in l:
	s += i
	if s > T:
		break
	cnt += 1
print(cnt)