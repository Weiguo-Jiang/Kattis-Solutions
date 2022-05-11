inp = input().split(';')
cnt = 0
for i in inp:
	j = list(map(int, i.split('-')))
	if len(j) == 1:
		cnt += 1
	else:
		cnt += j[1]-j[0]+1
print(cnt)