s = input()
l = len(s)
if len(s) % 2 == 1:
	print("fix")
else:
	if s[int(l/2)] == ')' and s[int(l/2-1)] == '(':
		print("correct")
	else:
		print("fix")