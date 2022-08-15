flag = 0
while True:
	grid = list()
	while True:
		try:
			inp = input()
			if len(inp) == 0:
				break
			grid.append([c for c in inp])
		except EOFError:
			flag = 1
			break
	
	columns = list()
	for i in range(len(grid[0])):
		l = list()
		for j in grid:
			l.append(j[i])
		columns.append(l)
	columns = sorted(columns, reverse=True)

	for i in range(len(grid)):
		l = list()
		for j in columns:
			l.append(j[i])
		print("".join(l))

	if not flag:
		print()

	if flag:
		break