d = dict()
def recur(depth, num, ub):
    if depth == 0:
        return 1

    if (depth, num) in d:
        return d[(depth, num)]

    if num == 0:
        s = recur(depth-1, 0, ub) + recur(depth-1, 1, ub)
    elif num == k:
        s = recur(depth-1, num-1, ub) + recur(depth-1, num, ub)
    else:
        s = recur(depth-1, num-1, ub) + recur(depth-1, num, ub) + recur(depth-1, num+1, ub)

    d[(depth, num)] = s
    return s

while True:
    try:
        k, n = map(int, input().split())
    except EOFError:
        break

    if k <= 1:
        print("100.000000000")
        continue

    comb = (k+1)**n
    cnt = 0
    for i in range(k+1):
        cnt += recur(n-1, i, k)
    print(cnt/comb*100)
    
    d = dict()