while True:
	try:
		inp = input().split()
	except EOFError:
		break
	start = inp[3].split(':')
	startM = int(start[0])*60+int(start[1])
	end = inp[4].split(':')
	endM = int(end[0])*60+int(end[1])

	d = endM - startM

	hour = d // 60
	minute = d % 60

	print(" ".join(inp[0:3]) + " " + str(hour) + " hours " + str(minute) + " minutes")