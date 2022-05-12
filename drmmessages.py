l = list(input())
l1 = l[0:len(l)//2]
l2 = l[len(l)//2:]
sum1 = 0
for i in l1:
	sum1 += (ord(i)-ord('A'))
for i in range(len(l1)):
	l1[i] = (sum1 + ord(l1[i]) - ord('A')) % 26
	l1[i] = chr(l1[i] + ord('A'))

sum2 = 0
for i in l2:
	sum2 += (ord(i)-ord('A'))
for i in range(len(l2)):
	l2[i] = (sum2 + ord(l2[i]) - ord('A')) % 26
	l2[i] = chr(l2[i] + ord('A'))

for i in range(len(l1)):
	print(chr((ord(l1[i])-ord('A')+ord(l2[i])-ord('A'))%26+ord('A')), end="")
print()
