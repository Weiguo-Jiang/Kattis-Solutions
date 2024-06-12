first = input()
last = input()
cnt = 0
for i in range(len(first)):
    if first[i] != last[i]:
        cnt += 1
print(cnt+1)