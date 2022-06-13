m , n = list(map(int, input().split()))
d = dict()
for i in range(m):
	job, value = input().split()
	value = int(value)
	d[job] = value

for i in range(n):
	s = 0
	while True:
		inp = input()
		if inp == '.':
			break
		inp = inp.split()
		for j in inp:
			if j in d:
				s += d[j]
	print(s)