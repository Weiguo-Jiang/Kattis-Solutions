import math
t = int(input())
for i in range(t):
	R, h1, h2 = list(map(float, input().split()))
	radian = math.acos(R/(R+h1/1000))+math.acos(R/(R+h2/1000))
	print(radian*R)