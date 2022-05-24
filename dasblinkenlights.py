p, q, s = list(map(int, input().split()))
flag = 0
for i in range(1, s+1):
	if i % p == 0 and i % q == 0:
		flag = 1
		break
if flag:
	print("yes")
else:
	print("no")