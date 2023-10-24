dic = dict()

def recur(you, opp, damage):
    if ("".join(map(str, you)), "".join(map(str, opp)), damage) in dic:
        return dic[("".join(map(str, you)), "".join(map(str, opp)), damage)]

    needed = 0
    for i in range(0, 7):
        needed += opp[i] * i
    if needed > damage:
        dic[("".join(map(str, you)), "".join(map(str, opp)), damage)] = 0
        return 0

    if sum(opp[1:]) == 0:
        dic[("".join(map(str, you)), "".join(map(str, opp)), damage)] = 1
        return 1

    p = []
    for i in range(1, 7):
        if you[i] > 0:
            copy = you[:]
            copy[i] -= 1
            copy[i - 1] += 1

            prob = recur(copy, opp, damage - 1)
            p.extend([prob] * you[i])

    for i in range(1, 7):
        if opp[i] > 0:
            copy = opp[:]
            copy[i] -= 1
            copy[i - 1] += 1

            prob = recur(you, copy, damage - 1)
            p.extend([prob] * opp[i])

    dic[("".join(map(str, you)), "".join(map(str, opp)), damage)] = sum(p) / len(p)
    return sum(p) / len(p)


n, m, d = map(int, input().split())
you = [0] * 7
opp = [0] * 7

l = list(map(int, input().split()))
for i in l:
    you[i] += 1

l = list(map(int, input().split()))
for i in l:
    opp[i] += 1

print(recur(you, opp, d))