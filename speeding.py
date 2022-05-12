n = int(input())
t = 0
d = 0
ans = 0
for i in range(n):
	t1, d1 = list(map(int, input().split()))
	if t1 == d1 == 0:
		continue
	s = (d1-d)/(t1-t)
	if s > ans:
		ans = s
	t = t1
	d = d1
print(int(ans))