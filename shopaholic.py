n = int(input())
inp = sorted(list(map(int, input().split())))
inp.reverse()
if n == 1 or n == 2:
	print(0)
else:
	discount = 0
	for i in range(2, len(inp), 3):
		discount += inp[i]
	print(discount)