while True:
	inp = input().split()
	if inp[0] == '0' and inp[1] == '0':
		break
	a = [int(i) for i in inp[0]]
	b = [int(i) for i in inp[1]]
	a.reverse()
	b.reverse()
	if len(a) > len(b):
		for i in range(len(a)-len(b)):
			b.append(0)
	elif len(a) < len(b):
		for i in range(len(b)-len(a)):
			a.append(0)

	carry = 0
	cnt = 0
	for i in range(len(a)):
		s = a[i] + b[i] + carry
		carry = 0
		if s >= 10:
			cnt += 1
			carry = 1
	
	if cnt == 0:
		print("No carry operation.")
	elif cnt == 1:
		print("1 carry operation.")
	else:
		print(str(cnt) + " carry operations.")