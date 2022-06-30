T = int(input())
for i in range(T):
	inp = input()
	if inp[0:10] == 'simon says':
		print(inp[11:])
	else:
		print()