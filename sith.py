name = input()
a = int(input())
b = int(input())
c = int(input())
a_b = a-b

ans = 'VEIT EKKI'

if a < b:
    if a_b == c:
        ans = 'Jedi'
    else:
        ans = 'Sith'

print(ans)