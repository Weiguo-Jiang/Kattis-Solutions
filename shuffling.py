def outShuffle(arr):
	l = len(arr)
	firstHalf = list()
	secondHalf = list()
	shuffled = list()
	if l%2 == 0:
		for i in range(l//2):
			firstHalf.append(arr[i])
		for i in range(l//2, l):
			secondHalf.append(arr[i])
		for i in range(l//2):
			shuffled.append(firstHalf[i])
			shuffled.append(secondHalf[i])
	else:
		for i in range(l//2+1):
			firstHalf.append(arr[i])
		for i in range(l//2+1, l):
			secondHalf.append(arr[i])
		for i in range(l//2):
			shuffled.append(firstHalf[i])
			shuffled.append(secondHalf[i])
		shuffled.append(firstHalf[-1])
	return shuffled


def inShuffle(arr):
	l = len(arr)
	firstHalf = list()
	secondHalf = list()
	shuffled = list()
	if l%2 == 0:
		for i in range(l//2):
			firstHalf.append(arr[i])
		for i in range(l//2, l):
			secondHalf.append(arr[i])
		for i in range(l//2):
			shuffled.append(secondHalf[i])
			shuffled.append(firstHalf[i])
	else:
		for i in range(l//2):
			firstHalf.append(arr[i])
		for i in range(l//2, l):
			secondHalf.append(arr[i])
		for i in range(l//2):
			shuffled.append(secondHalf[i])
			shuffled.append(firstHalf[i])
		shuffled.append(secondHalf[-1])
	return shuffled


inp = input().split()
n = int(inp[0])
inOrout = inp[1]
arr = list()
for i in range(n):
	arr.append(i)
c = arr

cnt = 0
if inOrout == 'in':
	while True:
		shuffled = inShuffle(arr)
		cnt += 1
		if shuffled == c:
			break
		arr = shuffled
else:
	while True:
		shuffled = outShuffle(arr)
		cnt += 1
		if shuffled == c:
			break
		arr = shuffled
print(cnt)