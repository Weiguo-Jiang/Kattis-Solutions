N = int(input())
for i in range(N):
	inp = input().split()
	c = 1 if inp[0] == 'F' else -1
	D = int(inp[1])
	H = int(inp[2])
	M = int(inp[3])

	minutes = M + c*D + H*60
	if minutes >= 24*60:
		minutes -= 24*60
	elif minutes < 0:
		minutes += 24*60

	print(str(minutes//60) + " " + str(minutes%60))
