l = list(map(int, input().split()))
ll = list()
for i in range(6):
	for j in range(i+1, 6):
		for k in range(j+1, 6):
			if l[i] + l[j] + l[k] == l[-2]:
				ll.append(l[i])
				ll.append(l[j])
				ll.append(l[k])
ll = [str(i) for i in sorted(ll)]
ll.reverse()
print(" ".join(ll), end=" ")

lll = list()
for i in range(6):
	if str(l[i]) not in ll:
		lll.append(l[i])
lll = [str(i) for i in sorted(lll)]
lll.reverse()
print(" ".join(lll))