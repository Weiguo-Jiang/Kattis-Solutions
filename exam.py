n = int(input())
s = input()
ss = input()

cnt1 = 0
cnt2 = 0

for i in range(len(s)):
	if s[i] == ss[i]:
		cnt1 += 1
	else:
		cnt2 += 1

if cnt1 <= n:
	print(cnt1 + len(s) - n)
else:
	print(n + cnt2)