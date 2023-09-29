N = int(input())
p = []
for i in range(N):
    p.append(float(input().split()[1]))
p.sort(reverse=True)

ans = 0
for i in range(1, N+1):
    ans += i * p[i-1]
print(ans)