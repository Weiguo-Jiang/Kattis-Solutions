import heapq
def neighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
heap = [(0, 0, 0)]
visited = set()
while heap:
    length, x, y = heapq.heappop(heap)
    if (x, y) in visited:
        continue
    visited.add((x, y))
    if x == M-1 and y == N-1:
        print(length)
        break
    for nx, ny in neighbors(x, y):
        if 0 <= nx < M and 0 <= ny < N:
            if (nx, ny) in visited:
                continue
            new_length = max(length, grid[nx][ny]-grid[x][y])
            heapq.heappush(heap, (new_length, nx, ny))