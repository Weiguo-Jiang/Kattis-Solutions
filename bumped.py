import heapq

n, m, f, s, t = map(int, input().split())
d = dict()
for _ in range(n):
    d[_] = dict()

for _ in range(m):
    i, j, c = map(int, input().split())
    if i not in d:
        d[i] = dict()
    else:
        d[i][j] = c
        d[j][i] = c

def dijkstra(s, t, d):
    q = [(0, s)]
    visited = set()
    while q:
        cost, u = heapq.heappop(q)
        if u == t:
            return cost
        if u in visited:
            continue
        visited.add(u)
        for v in d[u]:
            heapq.heappush(q, (cost + d[u][v], v))
    return float('inf')

minDist = dijkstra(s, t, d)

for _ in range(f):
    u, v = map(int, input().split())
    dist = dijkstra(s, u, d) + dijkstra(v, t, d)
    if dist < minDist:
        minDist = dist

print(minDist)