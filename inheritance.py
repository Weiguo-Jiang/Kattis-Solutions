l = []
def recur(n, P):
    if n > P:
        return

    global l
    if P % n == 0:
        l.append(n)

    recur(int(str(n) + '2'), P)
    recur(int(str(n) + '4'), P)

    return

n = int(input())
recur(2, n)
recur(4, n)
l.sort()
for i in l:
    print(i)