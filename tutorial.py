from math import log2

m, n, t = list(map(int, input().split()))
if t == 1:
	op = 1
	flag = 1
	for i in range(2, n+1):
		op *= i
		if op > m:
			print("TLE")
			flag = 0
			break
	if flag:
		print("AC")
elif t == 2:
	op = 1
	flag = 1
	for i in range(1, n+1):
		op *= 2
		if op > m:
			print("TLE")
			flag = 0
			break
	if flag:
		print("AC")
elif t == 3:
	if n**4 > m:
		print("TLE")
	else:
		print("AC")
elif t == 4:
	if n**3 > m:
		print("TLE")
	else:
		print("AC")
elif t == 5:
	if n**2 > m:
		print("TLE")
	else:
		print("AC")
elif t == 6:
	op = n*log2(n)
	if op > m:
		print("TLE")
	else:
		print("AC")
elif t == 7:
	if n > m:
		print("TLE")
	else:
		print("AC")