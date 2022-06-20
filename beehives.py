while True:
	d, N = list(map(float, input().split()))
	if N == 0:
		break
	dic = dict()
	N = int(N)
	l = list()
	for i in range(N):
		line = input()
		dic[line] = 1

		xy = list(map(float, line.split()))
		l.append(xy)

	for i in range(len(l)):
		for j in range(i+1, len(l)):
			square = (l[i][0]-l[j][0])**2 + (l[i][1]-l[j][1])**2
			if square < d**2:
				dic[str(l[i][0])+" "+str(l[i][1])] = 0
				dic[str(l[j][0])+" "+str(l[j][1])] = 0

	cnt = 0
	for key, value in dic.items():
		if value == 0:
			cnt += 1
	print(str(cnt) + " sour, " + str(N-cnt) + " sweet")
