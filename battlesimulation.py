l = [c for c in input()]
moves = list()
s = {'R', "B", "L"}
i = 0
while i < len(l):
	if i <= len(l)-3 and set(l[i:i+3]) == s:
		moves.append('C')
		i += 3
	else:
		if l[i] == 'R':
			moves.append('S')
		elif l[i] == 'B':
			moves.append('K')
		elif l[i] == 'L':
			moves.append('H')
		i += 1
print("".join(moves))