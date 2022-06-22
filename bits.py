T = int(input())
for i in range(T):
	X = int(input())
	maximum = 0
	while X != 0:
		bits = str(bin(X))
		cnt = 0
		for b in bits:
			if b == '1':
				cnt += 1
		if cnt > maximum:
			maximum = cnt
		X //= 10
	print(maximum)