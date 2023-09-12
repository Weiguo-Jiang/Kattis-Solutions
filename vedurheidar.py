v = int(input())
n = int(input())

for i in range(n):
    s, k = input().split()
    k = int(k)

    if k >= v:
        print(s + " opin")
    else:
        print(s + " lokud")