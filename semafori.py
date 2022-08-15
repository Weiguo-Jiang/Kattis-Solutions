N, L = list(map(int, input().split()))
t = 0
distance = 0
for i in range(N):
	D, R, G = list(map(int, input().split()))
	t += (D-distance)
	distance += (D-distance)
	if t % (R+G) < R:
		t += (R-t%(R+G))

t += (L-distance)
print(t)