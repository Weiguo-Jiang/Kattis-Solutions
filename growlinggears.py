n = int(input())
for i in range(n):
	t = int(input())
	maxTorque = -1
	gear = -1
	for j in range(t):
		a, b, c = list(map(int, input().split()))
		torque = -1*a*((b/(2*a))**2)+b*(b/(2*a))+c
		if torque > maxTorque:
			maxTorque = torque
			gear = j+1
	print(gear)
				