# https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

while True:
    n = int(input())
    if n == 0:
        break

    points = []
    for _ in range(n):
        x1, y1, x2, y2 = map(float, input().split())
        points.append(((x1, y1), (x2, y2)))

    d = {}
    for i in range(n):
        d[i] = []

    for i in range(n-1):
        for j in range(i+1, n):
            if intersect(points[i][0], points[i][1], points[j][0], points[j][1]):
                d[i].append(j)
                d[j].append(i)

    s = set()
    for i in range(n):
        for j in d[i]:
            for k in d[j]:
                if i in d[k] and j in d[k]:
                    s.add(tuple(sorted([i, j, k])))
    print(len(s))