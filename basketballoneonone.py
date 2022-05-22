s = input()
A = 0
B = 0
for i in range(0, len(s)-1, 2):
	if s[i] == 'A':
		A += int(s[i+1])
	else:
		B += int(s[i+1])
if A > B:
	print("A")
else:
	print("B")