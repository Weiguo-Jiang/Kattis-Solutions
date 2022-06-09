N, M = list(map(int, input().split()))
l = list()
for i in range(N):
	inp_list = [i for i in input()]
	l.append(inp_list)

cnt = 1
for i in range(M):
	flag = 1
	for j in l:
		if j[i] != '_':
			flag = 0
			break
	if flag:
		cnt += 1
print(cnt)