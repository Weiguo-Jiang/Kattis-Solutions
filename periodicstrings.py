def periodic(substr, s):
	rotations = [substr]
	substr = [i for i in substr]
	for i in range(len(substr)-1):
		c = substr[-1]
		substr.pop()
		substr.insert(0, c)
		rotations.append("".join(substr))

	duplicate = ("".join(rotations))*100
	if duplicate[0:len(s)] == s:
		return len(substr)
	return -1


s = input()
for i in range(1, len(s)+1):
	substr = s[0:i]
	if len(s)%len(substr) == 0:
		k = periodic(substr, s)
		if k == -1:
			continue
		else:
			print(k)
			break