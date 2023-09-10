s = input()
flag1 = 0
flag2 = 0

for i in range(len(s)-1):
    if s[i] == ':' and s[i+1] == ')':
        flag1 = 1
    elif s[i] == ':' and s[i+1] == '(':
        flag2 = 1

if flag1 and flag2:
    print("double agent")
elif flag1:
    print("alive")
elif flag2:
    print("undead")
else:
    print("machine")