N, P, S = list(map(int, input().split()))
for i in range(S):
	l = list(map(int, input().split()))
	flag = 0
	for j in range(1, l[0]+1):
		if l[j] == P:
			flag = 1
			break
	if flag:
		print("KEEP")
	else:
		print("REMOVE")
