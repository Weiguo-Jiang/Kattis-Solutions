s = input()
c = ""
ans = list()
for i in range(len(s)):
	if s[i] != c:
		ans.append(s[i])
		c = s[i]
print("".join(ans))