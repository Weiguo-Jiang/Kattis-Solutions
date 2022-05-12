s = input()
per = "PER"*(len(s)//3)
cnt = 0
for i in range(len(s)):
	if per[i] != s[i]:
		cnt += 1
print(cnt)