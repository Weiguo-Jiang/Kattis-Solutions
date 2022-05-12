R, C = list(map(int, input().split()))
m = list()
for i in range(R):
	r = [i for i in input()]
	m.append(r)

d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
for i in range(R-1):
	for j in range(C-1):
		if m[i][j] == '.' and m[i][j+1] == '.':
			if m[i+1][j] == '.' and m[i+1][j+1] == '.':
				d[0] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == 'X':
				d[2] += 1
			elif m[i+1][j] == '.' and m[i+1][j+1] == 'X':
				d[1] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == '.':
				d[1] += 1
		elif m[i][j] == 'X' and m[i][j+1] == 'X':
			if m[i+1][j] == '.' and m[i+1][j+1] == '.':
				d[2] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == 'X':
				d[4] += 1
			elif m[i+1][j] == '.' and m[i+1][j+1] == 'X':
				d[3] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == '.':
				d[3] += 1
		elif m[i][j] == '.' and m[i][j+1] == 'X':
			if m[i+1][j] == '.' and m[i+1][j+1] == '.':
				d[1] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == 'X':
				d[3] += 1
			elif m[i+1][j] == '.' and m[i+1][j+1] == 'X':
				d[2] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == '.':
				d[2] += 1
		elif m[i][j] == 'X' and m[i][j+1] == '.':
			if m[i+1][j] == '.' and m[i+1][j+1] == '.':
				d[1] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == 'X':
				d[3] += 1
			elif m[i+1][j] == '.' and m[i+1][j+1] == 'X':
				d[2] += 1
			elif m[i+1][j] == 'X' and m[i+1][j+1] == '.':
				d[2] += 1
for i in d:
	print(d[i])
