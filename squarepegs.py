N, M, K = list(map(int, input().split()))
radii = list(map(int, input().split()))
housesRadii = list()
circular = list(map(int, input().split()))
for i in circular:
	housesRadii.append(i)
square = list(map(int, input().split()))
for i in square:
	housesRadii.append(i/(2**0.5))
housesRadii.sort()
radii.sort()

cnt = 0
for i in radii:
	if cnt < M+K and i > housesRadii[cnt]:
		cnt += 1
print(cnt)