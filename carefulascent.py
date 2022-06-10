x, y = list(map(int, input().split()))
n = int(input())
s = 0
h = 0
for i in range(n):
	l, u, f = list(map(float, input().split()))
	s += (u-l)*f
	h += u-l
y -= h
s += y
print(x/s)