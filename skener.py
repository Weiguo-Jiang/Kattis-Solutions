R, C, ZR, ZC = map(int, input().split())
l = []
for i in range(R):
    ll = []
    inp = [c for c in input()]
    for j in inp:
        for k in range(ZC):
            ll.append(j)
    for j in range(ZR):
        l.append(ll)

for i in l:
    print(''.join(i))