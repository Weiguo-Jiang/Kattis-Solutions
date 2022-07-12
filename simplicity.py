w = [i for i in input()]
d = dict()
for i in w:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1
l = list()
for key, value in d.items():
	l.append(value)
l.sort()
if len(l) <= 2:
	print(0)
else:
	print(len(w)-l[-1]-l[-2])