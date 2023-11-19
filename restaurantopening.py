n, m = map(int, input().split())
d = dict()
for i in range(n):
    people = list(map(int, input().split()))
    for j in range(len(people)):
        d[(i, j)] = people[j]

minCost = float('inf')
for i in range(n):
    for j in range(m):
        curCost = 0
        location = (i, j)
        for key, value in d.items():
            curCost += (abs(key[0] - location[0]) + abs(key[1] - location[1])) * value
        minCost = min(minCost, curCost)
print(minCost)