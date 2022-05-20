while True:
	l = input()
	if len(l) == 1:
		break
	x1, y1, x2, y2, p = list(map(float, l.split()))
	print((abs((x1-x2)**p) + abs((y1-y2)**p))**(1/p))