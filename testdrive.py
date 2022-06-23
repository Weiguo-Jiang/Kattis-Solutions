a, b, c = list(map(int, input().split()))
d1 = b-a
d2 = c-b

if d1 == d2:
	print("cruised")
elif (d1 > 0 and d2 < 0) or (d2 > 0 and d1 < 0):
	print("turned")
elif abs(d2) > abs(d1):
	print("accelerated")
else:
	print("braked")