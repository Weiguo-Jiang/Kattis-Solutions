n = int(input())
for i in range(n):
	s = input()
	if s[0:10] == "Simon says":
		print(s[10:])