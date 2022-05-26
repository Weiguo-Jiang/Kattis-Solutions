import itertools

n = input()
l = [i for i in n]
s = set(itertools.permutations(l))

n = int(n)
m = 10**(len(str(n)))
flag = 0
for i in s:
	p = int("".join(i))
	if p > n and p < m:
		m = p
		flag = 1

if flag:
	print(m)
else:
	print('0')