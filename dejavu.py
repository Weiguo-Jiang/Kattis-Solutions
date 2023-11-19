N = int(input())
points = []
d1 = dict()
d2 = dict()
for i in range(1, 100001):
    d1[i] = 0
    d2[i] = 0
for _ in range(N):
    X, Y = map(int, input().split())
    points.append((X, Y))
    d1[X] += 1
    d2[Y] += 1

cnt = 0
for p in points:
    cnt += (d1[p[0]]-1)*(d2[p[1]]-1)
print(cnt)