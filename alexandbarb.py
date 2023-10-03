k, m, n = map(int, input().split())
ans = ''
if k%(m+n) < m:
    ans = 'Barb'
else:
    ans = 'Alex'
print(ans)