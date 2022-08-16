msg = [c for c in input()]
l = len(msg)
row = 0
i = 1
while i**2 <= l:
	if l % i == 0:
		row = i
	i += 1
column = l // row

ll = list()
i = 0
while i < l:
	ll.append(msg[i:i+row])
	i += row

l = list()
for i in range(row):
	for j in ll:
		l.append(j[i])
print("".join(l))