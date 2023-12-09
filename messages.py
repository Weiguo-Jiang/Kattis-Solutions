words = []
while True:
    word = input()
    if word == '#':
        break
    words.append(word)

strings = []
string = ''
while True:
    inp = input()
    if inp == '#':
        break
    if inp[-1] == '|':
        string += inp[:-1]
        strings.append(string)
        string = ''
    else:
        string += inp

for string in strings:
    tuples = []
    for word in words:
        # find all occurrences (i, j) of word in string
        i = 0
        while True:
            i = string.find(word, i)
            if i == -1:
                break
            tuples.append((i+len(word)-1, i))
            i += 1

    tuples.sort()

    cnt = 0
    end = -1
    for tp in tuples:
        if tp[1] > end:
            cnt += 1
            end = tp[0]
    print(cnt)