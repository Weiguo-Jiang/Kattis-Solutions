s = input()
index = 0
for i in s:
	if i != 'a':
		index += 1
	else:
		break
print(s[index:])