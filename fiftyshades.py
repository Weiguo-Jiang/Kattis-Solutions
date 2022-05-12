N = int(input())
cnt = 0
for i in range(N):
	w = input().lower()
	if "pink" in w or "rose" in w:
		cnt += 1
if cnt == 0:
	print("I must watch Star Wars with my daughter")
else:
	print(cnt)