class Trie:
    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
                current_dict['cnt'] += 1
            else:
                current_dict[letter] = {}
                current_dict = current_dict[letter]
                current_dict['cnt'] = 1

N = int(input())
trie = Trie()
for _ in range(N):
    word = input()
    trie.add(word)
    cur_dict = trie.root
    for letter in word:
        cur_dict = cur_dict[letter]
    print(cur_dict['cnt'] - 1)
