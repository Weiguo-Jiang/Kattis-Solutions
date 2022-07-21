n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
init = l[0:k]
d = dict()
for i in init:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1

minD = sorted(d)[len(d)-1] - sorted(d)[0]

for i in range(1, n-k+1):
	old = l[i-1]
	new = l[i+k-1]
	
	d[old] -= 1
	if d[old] == 0:
		d.pop(old)
	
	if new in d:
		d[new] += 1
	else:
		d[new] = 1

	currD = sorted(d)[len(d)-1] - sorted(d)[0]
	if currD < minD:
		minD = currD
print(minD)
