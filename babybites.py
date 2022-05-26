n = int(input())
l = input().split()
for i in range(len(l)):
	if l[i] != "mumble":
		l[i] = int(l[i])

flag = 1
cnt = 0
for i in l:
	if i == "mumble":
		cnt += 1
	else:
		if i != cnt + 1:
			print("something is fishy")
			flag = 0
			break
		else:
			cnt += 1
if flag:
	print("makes sense")