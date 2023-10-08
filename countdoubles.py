n, m = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
for i in range(n-m+1):
    ll = l[i:i+m]
    even = 0
    for j in ll:
        if j % 2 == 0:
            even += 1
    if even >= 2:
        cnt += 1
print(cnt)