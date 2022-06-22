d = dict()
while True:
	inp = input()
	if len(inp) == 0:
		break
	a, b = inp.split()
	d[b] = a

while True:
	try:
		inp = input()
	except EOFError:
		break

	if inp not in d:
		print("eh")
	else:
		print(d[inp])