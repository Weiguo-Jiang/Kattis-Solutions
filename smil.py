s = input()
l = []
for i in range(len(s)-2):
	if s[i] == ':' and s[i+1] == ')':
		l.append(i)
	elif s[i] == ';' and s[i+1] == ')':
		l.append(i)
	elif s[i] == ':' and s[i+1] == '-' and s[i+2] == ')':
		l.append(i)
	elif s[i] == ';' and s[i+1] == '-' and s[i+2] == ')':
		l.append(i)
if s[-2] == ':' and s[-1] == ')':
	l.append(len(s)-2)
elif s[-2] == ';' and s[-1] == ')':
	l.append(len(s)-2)
for i in l:
	print(i)