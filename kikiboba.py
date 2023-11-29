word = input()
b_cnt = word.count('b')
k_cnt = word.count('k')
if b_cnt > k_cnt:
    print("boba")
elif b_cnt < k_cnt:
    print("kiki")
elif b_cnt == k_cnt and b_cnt != 0:
    print("boki")
else:
    print("none")