ll = list()
while True:
	n = int(input())
	if n == 0:
		break
	l = list()
	for i in range(n):
		t = input().split()
		H, M = list(map(int, t[0].split(':')))
		if t[-1] == 'p.m.' and H == 12:
			l.append(720+M)
			continue
		elif t[-1] == 'a.m.' and H == 12:
			l.append(M)
			continue
		flag = 1 if t[-1] == 'p.m.' else 0
		minutes = H*60 + flag*720 + M
		l.append(minutes)

	l = sorted(l)
	case = list()
	for i in l:
		H = i // 60
		M = i % 60
		if M < 10:
			M = '0'+str(M)

		if i >= 0 and i <= 59:
			case.append("12:" + str(M) + " a.m.")
		elif i >= 720 and i <= 779:
			case.append("12:" + str(M) + " p.m.")
		else:
			if H > 12:
				case.append(str(H-12)+":"+str(M)+" p.m.")
			else:
				case.append(str(H)+":"+str(M)+" a.m.")
	
	ll.append(case)
	ll.append('\n')

for i in range(len(ll)-1):
	if ll[i] == '\n':
		print()
	else:
		print("\n".join(ll[i]))