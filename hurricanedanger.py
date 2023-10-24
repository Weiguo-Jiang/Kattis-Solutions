# https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    m = int(input())

    minD = 10000000
    minL = []
    for _ in range(m):
        city, x0, y0 = input().split()
        x0, y0 = int(x0), int(y0)
        d = abs((x2-x1)*(y1-y0)-(x1-x0)*(y2-y1))/((x2-x1)**2+(y2-y1)**2)**0.5

        if d < minD:
            minD = d
            minL = [city]
        elif d == minD:
            minL.append(city)
    print(" ".join(minL))