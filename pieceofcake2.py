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
n, h, v = list(map(int, input().split()))

h1 = n-h
v1 = n-v
# compare all four areas
print(4*max(h*v, h*v1, h1*v1, v*h1))