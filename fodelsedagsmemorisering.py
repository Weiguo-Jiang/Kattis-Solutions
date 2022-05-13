n = int(input())
d1 = dict()
d2 = dict()
for i in range(n):
	name, affection, birthday = input().split()
	affection = int(affection)
	d1[name] = affection
	d2[name] = birthday
d3 = dict()
for name, birthday in d2.items():
	if birthday not in d3:
		d3[birthday] = name
	else:
		if d1[d3[birthday]] < d1[name]:
			d3[birthday] = name
l = list()
for birthday, name in d3.items():
	l.append(name)
l = sorted(l)
print(len(l))
for i in l:
	print(i)