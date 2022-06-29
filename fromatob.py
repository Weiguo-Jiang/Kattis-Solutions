def minimum(a, b):
    if a == b:
        return 0

    if a < b:
        return b-a

    if a % 2 == 1:
        return 1 + minimum(a+1, b)
    else:
        return 1 + minimum(a//2, b)

a, b = list(map(int, input().split()))
print(minimum(a, b))