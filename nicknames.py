A = int(input())
prefixes = dict()
for i in range(A):
	name = input()
	for j in range(1, len(name)+1):
		prefix = name[0:j]
		if prefix in prefixes:
			prefixes[prefix] += 1
		else:
			prefixes[prefix] = 1

B = int(input())
for i in range(B):
	nickname = input()
	if nickname in prefixes:
		print(prefixes[nickname])
	else:
		print(0)