line = ''.join(input().split()).lower()
for i in range(len(line)-1):
    for j in range(i+1, len(line)):
        candidate = line[i:j+1]
        if candidate == candidate[::-1]:
            print("Palindrome")
            exit()
print("Anti-palindrome")