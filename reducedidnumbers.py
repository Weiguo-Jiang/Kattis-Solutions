G = int(input())
l = list()
s = set()
for i in range(G):
	SIN = int(input())
	l.append(SIN)

m = 1
while True:
	for i in l:
		s.add(i%m)
	if len(s) == G:
		break
	m += 1
	s = set()
print(m)