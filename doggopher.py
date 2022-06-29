x1, y1, x2, y2 = list(map(float, input().split()))
flag = 1
while True:
	try:
		inp = input().split()
		x, y = list(map(float, inp))
	except EOFError:
		break

	d1 = (x1-x)**2 + (y1-y)**2
	d2 = (x2-x)**2 + (y2-y)**2

	if 4*d1 <= d2:
		print("The gopher can escape through the hole at (" + inp[0] + "," + inp[1] + ").")
		flag = 0
		break
if flag:
	print("The gopher cannot escape.")