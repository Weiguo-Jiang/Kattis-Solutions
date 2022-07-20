n, d = list(map(int, input().split()))
l = list(map(int, input().split()))
dd = dict()
for i in l:
	if i//d in dd:
		dd[i//d].append(i)
	else:
		dd[i//d] = [i]

s = 0
for key, value in dd.items():
	ll = len(value)
	s += (ll*(ll-1)//2)
print(s)