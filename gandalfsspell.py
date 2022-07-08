s1 = input()
s2 = input().split()
if len(s1) != len(s2):
	print("False")
else:
	d1 = dict()
	d2 = dict()
	flag = 1
	for i in range(len(s1)):
		if s1[i] in d1 and d1[s1[i]] != s2[i]:
			print("False")
			flag = 0
			break
		elif s2[i] in d2 and d2[s2[i]] != s1[i]:
			print("False")
			flag = 0
			break

		d1[s1[i]] = s2[i]
		d2[s2[i]] = s1[i]
	if flag:
		print("True")