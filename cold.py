n = int(input())
ans = 0
temp = list(map(int, input().split()))
for i in range(n):
	if temp[i] < 0:
		ans += 1
print(ans)