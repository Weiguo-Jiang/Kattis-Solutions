n = int(input())
l = input()
ll = input()
flag = n % 2
f = 1
if flag == 0:
	for i in range(len(l)):
		if l[i] != ll[i]:
			print("Deletion failed")
			f = 0
			break
else:
	for i in range(len(l)):
		if l[i] == ll[i]:
			print("Deletion failed")
			f = 0
			break
if f:
	print("Deletion succeeded")
