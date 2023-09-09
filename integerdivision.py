#
# BEGIN-HEADER
#
# Name: Weiguo Jiang
#
# Student-ID: 1670913
#
# By submitting this code, you are agreeing that you have solved in accordance
# with the collaboration policy in CMPUT 303/403.
#
# END-HEADER
#

# get input
n, d = map(int, input().split())
l = list(map(int, input().split()))

dic = {}

# count number of same result
for i in l:
    if i//d in dic:
        dic[i//d] += 1
    else:
        dic[i//d] = 1

# number of pairs for each result is n*(n-1)/2
cnt = 0
for i in dic.values():
    cnt += i*(i-1)//2
print(cnt)