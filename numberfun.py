N = int(input())
for i in range(N):
	flag = 1
	a, b, c = list(map(int, input().split()))
	if a+b == c:
		print("Possible")
		flag = 0
	elif abs(a-b) == c:
		print("Possible")
		flag = 0
	elif a*b == c:
		print("Possible")
		flag = 0
	elif c*a == b:
		print("Possible")
		flag = 0
	elif c*b == a:
		print("Possible")
		flag = 0
	if flag:
		print("Impossible")