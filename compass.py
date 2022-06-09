n1 = int(input())
n2 = int(input())
degree = min(abs(n1-n2), 360-abs(n1-n2))
if degree == 180:
	print(180)
elif n2 > n1 and n2 - n1 < 180:
	print(degree)
elif n2 > n1 and n2 - n1 > 180:
	print(-1*degree)
elif n1 == n2:
	print(0)
elif n2 < n1 and n1 - n2 < 180:
	print(-1*degree)
elif n2 < n1 and n1 - n2 > 180:
	print(degree)