T = int(input())
for i in range(T):
	d = dict()
	cnt = 0
	m = -1
	n = int(input())
	for i in range(n):
		v = int(input())
		cnt += v
		d[i+1] = v
		if v > m:
			m = v
	l = list()
	flag = 1
	for key, value in d.items():
		if value == m:
			l.append(key)
		if len(l) > 1:
			flag = 0
			break
	percentage = m/cnt

	if not flag:
		print("no winner")
	elif percentage > 0.5:
		print("majority winner " + str(l[0]))
	else:
		print("minority winner " + str(l[0]))