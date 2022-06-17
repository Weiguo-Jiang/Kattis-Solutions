n = int(input())
flag = 1
for i in range(n):
	k = int(input())
	name = input()
	flag1 = 0
	flag2 = 0
	for j in range(k):
		item = input()
		if item == 'pea soup':
			flag1 = 1
		elif item == 'pancakes':
			flag2 = 1
	if flag1 and flag2:
		print(name)
		flag = 0
		break
if flag:
	print("Anywhere is fine I guess")