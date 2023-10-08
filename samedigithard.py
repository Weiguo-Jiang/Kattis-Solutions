A, B = map(int, input().split())
d = dict()
for x in range(A, B+1):
    for y in range(x, B+1):
        xy = x*y
        if xy not in range(A, B+1):
            break

        l1 = sorted([c for c in str(xy)])
        l2 = sorted([c for c in str(x)] + [c for c in str(y)])

        if l1 == l2:
            d[(x, y)] = xy

print("{0} digit-preserving pair(s)".format(len(d)))
for k in sorted(d.keys()):
    print("x = {0}, y = {1}, xy = {2}".format(k[0], k[1], d[k]))