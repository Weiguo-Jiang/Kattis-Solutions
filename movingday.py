n, V = list(map(int, input().split()))
m = -1
for i in range(n):
	l, w, h = list(map(int, input().split()))
	Vi = l*w*h
	if Vi > m:
		m = Vi
print(m-V)