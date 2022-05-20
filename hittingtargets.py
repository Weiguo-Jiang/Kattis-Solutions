m = int(input())
circles = list()
rectangles = list()
for i in range(m):
	s = input().split()
	if s[0] == 'rectangle':
		rectangles.append(list(map(int, s[1:])))
	elif s[0] == 'circle':
		circles.append(list(map(int, s[1:])))

n = int(input())
for i in range(n):
	cnt = 0
	x, y = list(map(int, input().split()))
	for j in circles:
		if (x-j[0])**2+(y-j[1])**2 <= j[2]**2:
			cnt += 1

	for j in rectangles:
		if x >= j[0] and x <= j[2] and y >= j[1] and y <= j[3]:
			cnt += 1
	print(cnt)