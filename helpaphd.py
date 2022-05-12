n = int(input())
for i in range(n):
	s = input()
	index = 0
	for i in s:
		if i == '+':
			break
		else:
			index += 1
	if index != len(s):
		print(str(int(s[:index])+int(s[index+1:])))
	else:
		print('skipped')