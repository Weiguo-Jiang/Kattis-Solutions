N = int(input())
l = sorted(list(map(int, input().split())))
l.append(-1)
start = l[0]
end = l[0]
ans = list()
for i in range(0, N):
	if l[i+1] == end + 1:
		end += 1
	else:
		if start == end:
			ans.append(str(start))
		elif start + 1 == end:
			ans.append(str(start))
			ans.append(str(end))
		else:
			ans.append(str(start)+'-'+str(end))
		start = l[i+1]
		end = l[i+1]
print(" ".join(ans))