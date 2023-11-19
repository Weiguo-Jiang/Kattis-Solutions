N = int(input())
l = []
for i in range(N):
    inp = input()
    if inp == "Present!":
        l.pop()
    else:
        l.append(inp)
if len(l) == 0:
    print("No Absences")
else:
    for i in l:
        print(i)