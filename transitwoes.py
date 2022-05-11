s, t, n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
cnt = 0
for i in range(n):
	cnt += d[i]
	mod = cnt % c[i]
	if mod != 0:
		cnt += (c[i] - mod)
	cnt += b[i]
cnt += d[n]
if cnt <= t:
	print("yes")
else:
	print("no")