n = int(input())
for i in range(n):
	s, d = list(map(int, input().split()))
	if (s+d)%2 != 0:
		print("impossible")
	else:
		a = (s+d)//2
		b = s-a
		if a < 0 or b < 0:
			print("impossible")
		elif a >= b:
			print(a, b)
		else:
			print(b, a)