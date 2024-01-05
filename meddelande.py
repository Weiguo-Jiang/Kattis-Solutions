N, M = map(int, input().split())
ans = ''
for _ in range(N):
    ans += input().replace('.', '')
print(ans)