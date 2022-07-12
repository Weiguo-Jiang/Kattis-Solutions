N, M = list(map(int, input().split()))
d = dict()
best = -1
for i in range(N):
	d[i] = 0
for i in range(N):
	ans = input().split()
	correctAns = list()
	for j in range(1, M+1):
		if j % 3 == 0 and j % 5 == 0:
			correctAns.append('fizzbuzz')
		elif j % 3 == 0:
			correctAns.append('fizz')
		elif j % 5 == 0:
			correctAns.append('buzz')
		else:
			correctAns.append(str(j))
	for j in range(M):
		if correctAns[j] == ans[j]:
			d[i] += 1

	if d[i] > best:
		best = d[i]

candidate = 1001
for key, value in d.items():
	if value == best and key < candidate:
		candidate = key
print(candidate+1)
