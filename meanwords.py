N = int(input())
words = [0]*46
cnt = [0]*46
for i in range(N):
    word = input()
    for j in range(len(word)):
        cnt[j] += 1
        words[j] += ord(word[j])

avg = []
i = 0
while cnt[i] != 0:
    avg.append(chr(words[i]//cnt[i]))
    i += 1
print(''.join(avg))