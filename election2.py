n = int(input())
d1 = dict()
for i in range(n):
	name = input()
	party = input()
	d1[name] = party

maximum = -1
m = int(input())
d2 = dict()
for i in range(m):
	name = input()
	if name not in d2:
		d2[name] = 1
	else:
		d2[name] += 1

	if d2[name] > maximum:
		maximum = d2[name]

cnt = 0
flag = 0
name = -1
for key, value in d2.items():
	if cnt == 2:
		flag = 1
		break
	if value == maximum:
		name = key
		cnt += 1

if flag:
	print("tie")
else:
	print(d1[name])