N = int(input())
for i in range(N):
	n = int(input())
	l = list(map(int, input().split()))
	d = dict()
	for j in l:
		if j in d:
			d[j] += 1
		else:
			d[j] = 1
	for key, value in d.items():
		if value == 1:
			print("Case #" + str(i+1) + ": " + str(key))