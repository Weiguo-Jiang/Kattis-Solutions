n = int(input())
l = [i for i in input()]
ans = 0
for i in range(n):
    for j in range(i, n):
        ll = l[i:j+1]
        d = dict()
        for k in ll:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
        s = set(d.values())
        if len(s) == 1:
            if len(ll) > ans:
                ans = len(ll)
print(ans)