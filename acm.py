d = dict()
penalty = 0
solved = 0

while True:
    inp = input().split()
    if inp[0] == '-1':
        break

    m = int(inp[0])
    p = inp[1]
    t = inp[2]

    if t == 'right':
        solved += 1
        if p in d:
            penalty += d[p] * 20
        penalty += m
    else:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1

print(solved, penalty)