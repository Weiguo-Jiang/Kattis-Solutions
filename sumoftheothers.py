while True:
	try:
		inp = list(map(int, input().split()))
	except EOFError:
		break
	print(sum(inp)//2)