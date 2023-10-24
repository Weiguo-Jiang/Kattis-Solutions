while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    best = ()
    bestRatio = float('inf')
    for _ in range(n):
        a, b = map(int, input().split())
        if a > m:
            continue
        ratio = b / a
        if ratio < bestRatio:
            bestRatio = ratio
            best = (a, b)
        elif ratio == bestRatio:
            if a > best[0]:
                best = (a, b)

    if best == ():
        print('No suitable tickets offered')
    else:
        print('Buy {} tickets for ${}'.format(best[0], best[1]))