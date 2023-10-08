n = int(input())
d = float(input())
winner = ''
cur_max = 0
for i in range(n):
    init, v, r = input().split()
    v = float(v)
    r = float(r)

    t = d/v
    rof = r/t
    eff = v/rof

    if eff > cur_max:
        winner = init
        cur_max = eff
print(winner)