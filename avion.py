ans = list()
for i in range(5):
	l = input()
	if "FBI" in l:
		ans.append(str(i+1))
if ans == []:
	print("HE GOT AWAY!")
else:
	print(" ".join(ans))