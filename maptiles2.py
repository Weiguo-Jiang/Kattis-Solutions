s = input()
print(len(s), end=" ")
a = 0
b = 0
for i in range(len(s)):
	a *= 2
	b *= 2
	if s[i] == '1':
		b += 1
	elif s[i] == '2':
		a += 1
	elif s[i] == '3':
		a += 1
		b += 1
print(b, end=" ")
print(a)