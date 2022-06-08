while True:
	inp = input()
	if inp == "0":
		break
	k, m = list(map(int, inp.split()))
	inp = set(input().split())
	flag = 1
	for i in range(m):
		cnt = 0
		cate = input().split()
		required = int(cate[1])
		length = int(cate[0])
		for j in range(length):
			if cate[2+j] in inp:
				cnt += 1
		if cnt < required:
			flag = 0
	if flag:
		print("yes")
	else:
		print("no")