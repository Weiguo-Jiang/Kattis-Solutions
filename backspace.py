inp = input()
l = list()
for i in inp:
	if i != '<':
		l.append(i)
	else:
		l.pop()
print("".join(l))