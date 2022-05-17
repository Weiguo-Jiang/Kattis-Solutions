ans = list()
while True:
	n = int(input())
	if n == 0:
		break
	l1 = list()
	d = dict()
	for i in range(n):
		m = int(input())
		l1.append(m)
		d[m] = i
	l1 = sorted(l1)
	for i in range(n):
		l1[i] = d[l1[i]]

	d1 = dict()
	l2 = list()
	for i in range(n):
		m = int(input())
		l2.append(m)
	l2 = sorted(l2)
	for i in range(n):
		d1[l1[i]] = l2[i]

	l = list()
	for i in range(n):
		l.append(d1[i])
	ans.append(l)

for i in range(len(ans)-1):
	for j in ans[i]:
		print(j)
	print()

for i in ans[len(ans)-1]:
	print(i)
