y = int(input())
l = (y-2018)*12-4
u = (y-2018)*12+8
flag = 1
for i in range(l+1, u+1):
	if i % 26 == 0:
		print("yes")
		flag = 0
		break
if flag:
	print("no")