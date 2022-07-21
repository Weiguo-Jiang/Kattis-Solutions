A, B = list(map(int, input().split()))
l = list()
for i in range(97, 123):
	for j in range(97, 123):
		for k in range(97, 123):
			for m in range(97, 103):
				l.append(chr(i)+chr(j)+chr(k)+chr(m))
print(" ".join(l[0:max(A, B//2+1)]))