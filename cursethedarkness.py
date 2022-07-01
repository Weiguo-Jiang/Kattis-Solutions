m  =int(input())
for i in range(m):
	X, Y = list(map(float, input().split()))
	n = int(input())
	flag = 1
	for j in range(n):
		x, y = list(map(float, input().split()))
		if not flag:
			continue
		d = (X-x)**2+(Y-y)**2
		if d <= 64:
			flag = 0
	if flag:
		print("curse the darkness")
	else:
		print("light a candle")