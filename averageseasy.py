T = int(input())
blank = input()
for i in range(T):
	NCS, NE = list(map(int, input().split()))
	l = list()
	while True:
		try:
			line = list(map(int, input().split()))
		except EOFError:
			break
		if len(line) == 0:
			break

		for n in line:
			l.append(n)

	sumCS = 0
	for j in range(NCS):
		sumCS += l[j]
	avgCS = sumCS/NCS

	sumNE = 0
	for j in range(NCS, NE+NCS):
		sumNE += l[j]
	avgNE = sumNE/NE

	cnt = 0
	for j in range(NCS):
		if (sumCS-l[j])/(NCS-1) > avgCS and (sumNE+l[j])/(NE+1) > avgNE:
			cnt += 1
	print(cnt)