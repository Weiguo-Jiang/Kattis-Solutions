# https://en.wikipedia.org/wiki/Rotation_matrix

from math import radians, sin, cos

def remove_middle(a, b, c):
    cross = (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
    dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
    return cross < 0 or cross == 0 and dot <= 0

def convex_hull(points):
    spoints = sorted(points)
    hull = []
    for p in spoints + spoints[::-1]:
        while len(hull) >= 2 and remove_middle(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull

area = lambda *p: abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(p, p[1:] + p[:1]))) / 2

N = int(input())
for i in range(N):
    n = int(input())
    points = []
    boardArea = 0
    for j in range(n):
        x, y, w, h, v = map(float, input().split())
        v = radians(-v)

        rotated1 = (x + cos(v)*w/2 - sin(v)*h/2, y + sin(v)*w/2 + cos(v)*h/2)
        rotated2 = (x - cos(v)*w/2 - sin(v)*h/2, y - sin(v)*w/2 + cos(v)*h/2)
        rotated3 = (x - cos(v)*w/2 + sin(v)*h/2, y - sin(v)*w/2 - cos(v)*h/2)
        rotated4 = (x + cos(v)*w/2 + sin(v)*h/2, y + sin(v)*w/2 - cos(v)*h/2)

        points.extend([rotated1, rotated2, rotated3, rotated4])

        boardArea += w*h

    hull = convex_hull(points)
    hullArea = area(*hull)
    print('{:.1f} %'.format(boardArea / hullArea * 100))