s = input()
i = 0
ans = ""
while i < len(s):
	if s[i:i+3] == 'apa':
		ans += 'a'
		i += 3
	elif s[i:i+3] == 'epe':
		ans += 'e'
		i += 3
	elif s[i:i+3] == 'ipi':
		ans += 'i'
		i += 3
	elif s[i:i+3] == 'opo':
		ans += 'o'
		i += 3
	elif s[i:i+3] == 'upu':
		ans += 'u'
		i += 3
	else:
		ans += s[i]
		i += 1
print(ans)