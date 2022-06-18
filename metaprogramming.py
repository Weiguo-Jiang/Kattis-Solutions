d = dict()
while True:
	try:
		inp = input().split()
	except EOFError:
		break
	if inp[0] == 'define':
		d[inp[2]] = int(inp[1])

	if inp[0] == 'eval':
		if (inp[1] not in d) or (inp[3] not in d):
			print("undefined")
		else:
			if inp[2] == '=':
				if d[inp[1]] == d[inp[3]]:
					print("true")
				else:
					print("false")
			elif inp[2] == '>':
				if d[inp[1]] > d[inp[3]]:
					print("true")
				else:
					print("false")
			else:
				if d[inp[1]] < d[inp[3]]:
					print("true")
				else:
					print("false")
