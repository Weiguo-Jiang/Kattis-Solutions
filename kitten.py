n = input()
d = dict()

while True:
	l = input().split()
	if l[0] == "-1":
		break
	for i in range(1, len(l)):
		d[l[i]] = l[0]

l = [n]
while True:
	if n not in d:
		break
	else:
		l.append(d[n])
		n = d[n]

print(" ".join(l))