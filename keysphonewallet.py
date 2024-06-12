N = int(input())
l = ['keys', 'phone', 'wallet']
for i in range(N):
    obj = input()
    if obj in l:
        l.remove(obj)

if l:
    for i in l:
        print(i)
else:
    print("ready")
