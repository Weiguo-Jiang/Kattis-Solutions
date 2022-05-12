n = int(input())
area = 0
x, y = list(map(float, input().split()))
for i in range(n-1):
	x1, y1 = list(map(float, input().split()))
	area += (y+y1)*(x1-x)/2
	x = x1
	y = y1
print(area/1000)