C, X, M = list(map(float, input().split()))
speed = -1
fuel = C / 2
flag = 0
for i in range(6):
	MPH, MPG = list(map(float, input().split()))
	fuelNeeded = M / MPG + M / MPH * X
	if fuelNeeded <= fuel:
		speed = MPH
		flag = 1
if flag:
	print("YES " + str(int(speed)))
else:
	print("NO")