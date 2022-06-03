N = int(input())
case = 1
for i in range(N):
	S = int(input())
	B = list()
	R = list()
	rp = input().split()
	for r in rp:
		if r[-1] == 'R':
			R.append(int(r[0:len(r)-1]))
		else:
			B.append(int(r[0:len(r)-1]))

	B = sorted(B)
	R = sorted(R)
	if len(B) == 0 or len(B) == 0:
		print('Case #' + str(case) + ": 0")
	else:
		cnt = 0
		l = 0
		m = min(len(B), len(R))
		for k in range(m):
			l += (B[-1-k]+R[-1-k])
			cnt += 2
		l -= cnt
		print('Case #' + str(case) + ": " + str(l))
	
	case += 1
