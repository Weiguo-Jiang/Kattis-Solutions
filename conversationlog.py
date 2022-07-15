M = int(input())
d1 = dict()
d2 = dict()
s = set()
for i in range(M):
	message = input().split()
	name = message[0]
	for j in message:
		if j not in d1:
			d1[j] = 1
		else:
			d1[j] += 1
	if name not in d2:
		d2[name] = set(message[1:])
	else:
		for j in message[1:]:
			d2[name].add(j)
	for j in message[1:]:
		s.add(j)

for key, value in d2.items():
	s = s & value

if len(s) == 0:
	print("ALL CLEAR")
else:
	s2 = set()
	for i in s:
		s2.add(d1[i])
	l = sorted(list(s2))
	
	while len(l) != 0:
		ll = list()
		for i in s:
			if d1[i] == l[-1]:
				ll.append(i)
		ll.sort()
		for i in ll:
			print(i)
		l.pop()
