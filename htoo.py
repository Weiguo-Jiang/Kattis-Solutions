def formulaToDict(l, d):
	c = l[0]
	n = ""
	for i in range(1, len(l)):
		if l[i] >= '0' and l[i] <= '9':
			n += l[i]
		else:
			if len(n) == 0:
				if c in d:
					d[c] += 1
				else:
					d[c] = 1
			else:
				if c in d:
					d[c] += int(n)
				else:
					d[c] = int(n)
			c = l[i]
			n = ""


l, k = input().split()
l += 'a'
k = int(k)

d1 = dict()
formulaToDict(l, d1)

l = input() + 'a'
d2 = dict()
formulaToDict(l, d2)

cnt = 2**32
for element in d2:
	if element not in d1:
		cnt = 0
		break

	n = int(k*d1[element]/d2[element])
	if n < cnt:
		cnt = n
print(cnt)
