case = 1
while True:
	try:
		inp = sorted([int(i) for i in input().split()[1:]])
	except EOFError:
		break
	print("Case " + str(case) + ": " + str(inp[0]) + " " + str(inp[-1]) + " " + str(inp[-1]-inp[0]))
	case += 1