def prime(n):
	for i in range(2, int((n**0.5))+1):
		if n%i == 0:
			return 0
	return 1


n = int(input())
for i in range(n):
	x = int(input())
	cnt = 0
	l = list()
	for j in range(2, x//2+1):
		if prime(j) and prime(x-j):
			cnt += 1
			l.append(str(j)+"+"+str(x-j))

	print(str(x) + " has " + str(cnt) + " representation(s)")
	for j in l:
		print(j)
	print()