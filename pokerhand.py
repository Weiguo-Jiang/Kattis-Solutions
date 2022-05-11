l = input().split()
d = dict()
for i in l:
	if i[0] in d:
		d[i[0]] += 1
	else:
		d[i[0]] = 1
ans = 0
for i in d.values():
	if i > ans:
		ans = i
print(ans)