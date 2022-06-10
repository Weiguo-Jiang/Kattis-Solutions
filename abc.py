d = dict()
l = sorted([int(i) for i in input().split()])
d['A'] = l[0]
d['B'] = l[1]
d['C'] = l[2]
inp = input()
l = list()
for i in inp:
	l.append(str(d[i]))
print(" ".join(l))