n, e = list(map(int, input().split()))
cnt = 0
pw = str(2**e)
for i in range(1, n+1):
	if pw in str(i):
		cnt += 1
print(cnt)