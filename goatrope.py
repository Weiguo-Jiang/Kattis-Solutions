x, y, x1, y1, x2, y2 = list(map(int, input().split()))
minimum = 1000000000
if x >= x1 and x <= x2:
	d = min(abs(y1-y), abs(y2-y))
	if d < minimum:
		minimum = d

if y >= y1 and y <= y2:
	d = min(abs(x1-x), abs(x2-x))
	if d < minimum:
		minimum = d

d1 = ((x1-x)**2+(y-y1)**2)**0.5
d2 = ((x2-x)**2+(y-y2)**2)**0.5
d3 = ((x1-x)**2+(y-y2)**2)**0.5
d4 = ((x2-x)**2+(y-y1)**2)**0.5
d = min(d1, d2, d3, d4)
if minimum > d:
	minimum = d

print(minimum)