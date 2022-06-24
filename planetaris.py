n, a = list(map(int, input().split()))
inp = sorted(list(map(int, input().split())))
cnt = 0
s = 0
for i in inp:
	s += (i+1)
	if s > a:
		break
	cnt += 1
print(cnt)