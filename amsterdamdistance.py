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

from math import pi

# get input
l = input().split()
M = int(l[0])
N = int(l[1])
R = float(l[2])
a_x, a_y, b_x, b_y = map(int, input().split())

# keep track of the least distance
least = (a_y + b_y) / N * R

# iterate over different half-rings
for i in range(1, min(a_y, b_y)+1):
    # calculate radius of arc
    r = i/N*R

    # distance via this path
    distance = pi*r*abs(a_x-b_x)/M + (a_y + b_y)/N*R - 2*i/N*R

    least = min(distance, least)

print(least)