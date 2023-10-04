import heapq

M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

def neighbors(i, j):
    if (i, j) == (0, 0):
        return [(0, 1), (1, 0)]
    elif (i, j) == (0, N-1):
        return [(0, N-2), (1, N-1)]
    elif (i, j) == (M-1, 0):
        return [(M-2, 0), (M-1, 1)]
    elif (i, j) == (M-1, N-1):
        return [(M-2, N-1), (M-1, N-2)]
    elif i == 0:
        return [(0, j-1), (0, j+1), (1, j)]
    elif i == M-1:
        return [(M-1, j-1), (M-1, j+1), (M-2, j)]
    elif j == 0:
        return [(i-1, 0), (i+1, 0), (i, 1)]
    elif j == N-1:
        return [(i-1, N-1), (i+1, N-1), (i, N-2)]
    else:
        return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

