N, S, R = map(int, input().split())
damaged = list(map(int, input().split()))
reserved = list(map(int, input().split()))
l = [-1] + [1]*N + [-1]

for i in damaged:
    l[i] -= 1

for i in reserved:
    l[i] += 1

for i in range(1, len(l)-1):
    if l[i-1] == 0 and l[i] == 2:
        l[i-1] = 1
        l[i] = 1
    elif l[i+1] == 0 and l[i] == 2:
        l[i+1] = 1
        l[i] = 1

cnt = 0
for i in l:
    if i == 0:
        cnt += 1
print(cnt)
