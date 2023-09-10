t, n = map(int, input().split())

s = t*60

l = sorted(list(map(int, input().split())))

ans = 0
for i in l:
    if s - i < 0:
        break
    ans += i
    s -= i

print(ans)