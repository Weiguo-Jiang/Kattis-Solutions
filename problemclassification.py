N = int(input())
d = dict()
for i in range(N):
	cate = input().split()
	d[cate[0]] = set()
	for j in cate[2:]:
		d[cate[0]].add(j)

cnt = dict()
for key in d:
	cnt[key] = 0
freq = 0
while True:
	try:
		l = input().split()
	except EOFError:
		break

	for i in l:
		for key, value in d.items():
			if i in value:
				cnt[key] += 1
				if cnt[key] > freq:
					freq = cnt[key]
l = list()
for key, value in cnt.items():
	if value == freq:
		l.append(key)
l.sort()
for i in l:
	print(i)