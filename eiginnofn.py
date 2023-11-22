n = int(input())
d = dict()
for _ in range(n):
    given = list(input().split())
    d[given[0]] = given

m = int(input())
for _ in range(m):
    query = input()
    if query not in d:
        print("Neibb")
    elif len(d[query]) == 1:
        print("Jebb")
    else:
        print("Neibb en {0} {1} er heima".format(d[query][0], d[query][1]))