L = int(input())
D = int(input())
X = int(input())
N = 0
M = 0
for i in range(L, D+1):
	j = i
	s = 0
	while i != 0:
		d = i % 10
		s += d
		i = i // 10
	if s == X:
		print(j)
		break

for i in range(D, L-1, -1):
	j = i
	s = 0
	while i != 0:
		d = i % 10
		s += d
		i = i // 10
	if s == X:
		print(j)
		break