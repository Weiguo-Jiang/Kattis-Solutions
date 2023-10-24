from math import ceil
def factors(n):
    l = []
    for i in range(1, ceil(n**0.5)):
        if n % i == 0:
            l.append((i, n//i))
            l.append((n//i, i))
    if int(n**0.5)**2 == n:
        l.append((int(n**0.5), int(n**0.5)))
    return l

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())

    la = factors(a)
    lc = factors(c)

    flag = False
    for i in la:
        for j in lc:
            if i[0]*j[1] + i[1]*j[0] == b:
                print("YES")
                flag = True
                break
        if flag:
            break
    if not flag:
        print("NO")