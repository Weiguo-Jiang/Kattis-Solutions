import math
while True:
	r, h, s = list(map(int, input().split()))
	if r == 0 and h == 0 and s == 0:
		break

	radian = math.acos(r/h)
	arc = (math.pi/2-radian)*r
	l = (h**2-r**2)**0.5

	ans = (2*l+2*arc+math.pi*r)*(1+s/100)

	print('{0:.2f}'.format(ans))