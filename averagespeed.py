seconds = 0
speed = 0
d = 0

while True:
	try:
		l = input().split()
	except EOFError:
		break

	currT = [int(i) for i in l[0].split(':')]
	currSeconds = currT[0]*3600+currT[1]*60+currT[2]

	if len(l) == 2:
		newSpeed = int(l[1])
		timeD = currSeconds-seconds
		d += (timeD*speed/3600)

		speed = newSpeed
		seconds = currSeconds
	else:
		timeD = currSeconds-seconds
		d += (timeD*speed/3600)

		seconds = currSeconds
		print(l[0], end=" ")
		print("{:.2f}".format(round(d, 2)), end=" ")
		print("km")