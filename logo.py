import math

T = int(input())
for i in range(T):
	n = int(input())
	x = 0
	y = 0
	degree = 0
	for j in range(n):
		c, d = input().split()
		d = int(d)

		if c == 'lt':
			degree += d

		elif c == 'rt':
			degree -= d

		elif c == 'fd':
			dx = d*math.cos(degree/180*math.pi)
			dy = d*math.sin(degree/180*math.pi)
			x += dx
			y += dy

		elif c == 'bk':
			dx = d*math.cos(degree/180*math.pi)
			dy = d*math.sin(degree/180*math.pi)
			x -= dx
			y -= dy

	print(int(round((x**2+y**2)**0.5, 0)))