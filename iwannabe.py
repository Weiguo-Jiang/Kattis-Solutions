N, K = list(map(int, input().split()))
Attack = dict()
Defense = dict()
Health = dict()
n = 0
for i in range(N):
	A, D, H = list(map(int, input().split()))
	Attack[A] = n
	Defense[D] = n
	Health[H] = n
	n += 1

Attack = sorted(Attack.items())
Defense = sorted(Defense.items())
Health = sorted(Health.items())
Attack.reverse()
Defense.reverse()
Health.reverse()

s = set()
for i in range(K):
	s.add(Attack[i][1])
	s.add(Defense[i][1])
	s.add(Health[i][1])
print(len(s))