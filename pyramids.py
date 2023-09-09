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

# number of blocks
N = int(input())

# height
h = 0

while N >= 0:
    # current height has width 2*h+1
    N -= (2*h+1)**2
    if N < 0:
        break
    h += 1

print(h)
