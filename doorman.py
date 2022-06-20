def swap(arr, i, j):
	c = arr[i]
	arr[i] = arr[j]
	arr[j] = c


X = int(input())
line = [i for i in input()]
W = 0
M = 0
flag = 1
for i in range(len(line)-1):
	if W-M == X and line[i] == 'W':
		if line[i+1] == 'M':
			swap(line, i, i+1)
		else:
			flag = 0
			break
	elif M-W == X and line[i] == 'M':
		if line[i+1] == 'W':
			swap(line, i, i+1)
		else:
			flag = 0
			break

	if line[i] == 'W':
		W += 1
	else:
		M += 1

if flag:
	if line[len(line)-1] == 'W' and abs(W+1-M) <= X:
		W += 1
	elif line[len(line)-1] == 'M' and abs(M+1-W) <= X:
		M += 1
print(W+M)