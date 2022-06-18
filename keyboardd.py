s = [i for i in input()]
d1 = dict()
for i in s:
	if i not in d1:
		d1[i] = 1
	else:
		d1[i] += 1

t = [i for i in input()]
d2 = dict()
for i in t:
	if i not in d2:
		d2[i] = 1
	else:
		d2[i] += 1

l = list()
for i in d1:
	if d1[i] < d2[i]:
		l.append(i)
print("".join(l))
