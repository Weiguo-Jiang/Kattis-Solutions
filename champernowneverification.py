# generate all champernowne numbers up to 10^9
# and verify the correctness of the solution

dic = {}
s = ''
for i in range(1, 11):
    s += str(i)
    dic[s] = i

inp = input()
print(dic[inp] if inp in dic else -1)
