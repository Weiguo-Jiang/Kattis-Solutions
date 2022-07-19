alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input()
l = list()
for i in range(len(s)+1):
	l.append([0 for j in range(27)])

def lcs():
	for i in range(len(s)):
		for j in range(26):
			if s[i] == alphabet[j]:
				l[i+1][j+1] = 1+l[i][j]
			else:
				l[i+1][j+1] = max(l[i][j+1], l[i+1][j])

lcs()
print(26-l[-1][-1])
