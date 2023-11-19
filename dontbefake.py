N = int(input())
d = dict()
for i in range(86400):
    d[i] = 0
for _ in range(N):
    inp = list(map(int, input().split()))
    pairs = [(inp[i], inp[i+1]) for i in range(1, len(inp), 2)]
    for pair in pairs:
        for i in range(pair[0], pair[1]+1):
            d[i] += 1

Max = 0
cnt = 0
for i in range(86400):
    if d[i] > Max:
        Max = d[i]
        cnt = 1
    elif d[i] == Max:
        cnt += 1
print(Max)
print(cnt)