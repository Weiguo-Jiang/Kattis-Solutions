letters = [i for i in input()]
n = int(input())
for i in range(n):
	inp = input()
	if letters[0] not in inp:
		continue
	if len(inp) < 4:
		continue

	flag = 1
	
	for j in inp:
		if j not in letters:
			flag = 0
	if flag:
		print(inp)