hallway = input()
d = dict()
for i in range(len(hallway)):
    if hallway[i] == '>':
        d[i] = 0
    elif hallway[i] == '<':
        for key in d:
            d[key] += 1
print(sum(d.values()))