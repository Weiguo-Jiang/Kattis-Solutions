d = dict()
while True:
	inp = input()
	if inp == "***":
		break
	if inp not in d:
		d[inp] = 1
	else:
		d[inp] += 1
m = -1
for key, value in d.items():
	if value > m:
		m = value
l = list()
flag = 1
for key, value in d.items():
	if value == m:
		l.append(key)
	if len(l) > 1:
		flag = 0
		break
if flag:
	print(l[0])
else:
	print("Runoff!")