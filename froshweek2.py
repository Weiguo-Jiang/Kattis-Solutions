n, m = list(map(int, input().split()))
tasks = sorted(list(map(int, input().split())))
quiet = sorted(list(map(int, input().split())))

cnt = 0

i = 0
for t in tasks:
	while True:
		if i < len(quiet) and t <= quiet[i]:
			cnt += 1
			i += 1
			break
		elif i >= len(quiet):
			break
		i += 1
print(cnt)