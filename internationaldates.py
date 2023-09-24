date = list(map(int, input().split('/')))
ans = 'either'

if date[0] > 12:
    ans = 'EU'
elif date[1] > 12:
    ans = 'US'

print(ans)