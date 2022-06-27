import math
H, v = list(map(int, input().split()))
if v >= 0 and v <= 180:
	print("safe")
else:
	print(int(H/abs(math.sin(v/180*math.pi))))