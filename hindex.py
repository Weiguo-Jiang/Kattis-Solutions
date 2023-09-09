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
n = int(input())
l = []
for i in range(n):
    c = int(input())
    l.append(c)

l.sort()
l.reverse()

# try until H is too big
H = 0
for i in range(n):
    if l[i] >= i+1:
        H = i+1
    else:
        break
print(H)