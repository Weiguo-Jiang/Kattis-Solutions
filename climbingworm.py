a, b, h = list(map(int, input().split()))
cnt = 0
currH = 0
while True:
	cnt += 1
	currH += a
	if currH >= h:
		break
	currH -= b
print(cnt)