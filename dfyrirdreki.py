a = int(input())
b = int(input())
c = int(input())

# b^2 - 4ac
d = b**2 - 4*a*c
print(0 if d < 0 else 1 if d == 0 else 2)