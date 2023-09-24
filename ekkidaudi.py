l1 = input().split('|')
l2 = input().split('|')
l = []
for i in range(len(l1)):
    l.append(l1[i] + l2[i] + " ")
l = "".join(l)
print(l[:-1])