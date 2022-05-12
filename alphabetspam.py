s = input()
whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0
for i in s:
	if i == '_':
		whitespace += 1
	elif i.islower():
		lowercase += 1
	elif i.isupper():
		uppercase += 1
	else:
		symbols += 1
l = len(s)
print(whitespace/l)
print(lowercase/l)
print(uppercase/l)
print(symbols/l)