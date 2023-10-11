n = int(input())
result = 1
for i in range(n):
    a, op, b = input().split()
    a = int(a)
    b = int(b)

    if op == '*':
        result = (a*b)**2
    elif op == '+':
        result = (a+b) - result
    elif op == '-':
        result *= (a-b)
    elif op == '/':
        if a%2 == 0:
            result = a//2
        else:
            result = a//2 + 1

    print(result)