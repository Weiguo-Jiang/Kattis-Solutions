n = int(input())
words = input().split()
l = []
for word in words:
    if word[0].isupper():
        l.append(word[0])
print("".join(l))