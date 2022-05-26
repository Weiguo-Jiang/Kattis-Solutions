a = input()
b = input()

l1 = list()
l2 = list()
if len(a) >= len(b):
	for i in range(len(a)-len(b)):
		l2.append(0)
	for i in b:
		l2.append(int(i))
	l1 = [int(i) for i in a]
else:
	for i in range(len(b)-len(a)):
		l1.append(0)
	for i in a:
		l1.append(int(i))
	l2 = [int(i) for i in b]

l3 = list()
m = max(len(l1), len(l2))
carry = 0
for i in range(m-1, -1, -1):
	n = l1[i]+l2[i]+carry
	if n >= 10:
		carry = 1
		l3.append(n%10)
	else:
		carry = 0
		l3.append(n)

if carry == 1:
	l3.append(1)

for i in range(len(l3)-1, 0, -1):
	print(l3[i], end="")
print(l3[0])