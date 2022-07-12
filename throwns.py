n, k = list(map(int, input().split()))
inp = input().split()
l = list()
for i in range(len(inp)):
	if inp[i] == 'undo':
		for j in range(int(inp[i+1])):
			l.pop()
		inp[i+1] = 'e'
	elif inp[i] == 'e':
		continue
	else:
		l.append(int(inp[i]))
print(sum(l)%n)