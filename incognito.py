T = int(input())
for i in range(T):
	n = int(input())
	d = dict()
	for i in range(n):
		name, cate = input().split()
		if cate in d:
			d[cate] += 1
		else:
			d[cate] = 1
	if n == 0:
		print(0)
	else:
		cnt = 1
		for key, value in d.items():
			cnt *= (value+1)
		print(cnt-1)