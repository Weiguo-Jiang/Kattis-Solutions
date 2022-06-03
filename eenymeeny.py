l = len(input().split())
n = int(input())
ll = list()
for i in range(n):
	name = input()
	ll.append(name)

t1 = list()
t2 = list()

index = -1

flag = 1
while len(ll) != 0:
	for i in range(l):
		index += 1
		if index == len(ll):
			index = 0
	if flag:
		t1.append(ll[index])
		flag = 0
	else:
		t2.append(ll[index])
		flag = 1
	ll.remove(ll[index])
	index -= 1
print(len(t1))
for i in t1:
	print(i)
print(len(t2))
for i in t2:
	print(i)
