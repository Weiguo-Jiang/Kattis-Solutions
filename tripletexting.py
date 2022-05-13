s = input()
n = len(s)//3
s1 = s[:n]
s2 = s[n:2*n]
s3 = s[2*n:]
if s1 == s2:
	print(s1)
elif s1 == s3:
	print(s1)
elif s2 == s3:
	print(s2)