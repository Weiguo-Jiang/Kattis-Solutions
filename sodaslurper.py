e, f, c = list(map(int, input().split()))
s = e+f
cnt = 0
while True:
	s -= c
	if s < 0:
		break
	cnt += 1
	s += 1
print(cnt)