N, M = map(int, input().split())
prohibition = [0]*N

for i in range(M):
    a, b = map(int, input().split())
    prohibition[a-1] |= 1 << (b-1)
    prohibition[b-1] |= 1 << (a-1)

def make(cur, at):
    if at == N:
        return 1
    if prohibition[at] & cur:
        return make(cur, at+1)
    return make(cur | (1 << at), at+1) + make(cur, at+1)

print(make(0, 0))