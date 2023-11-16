class SegmentTree:
    def __init__(self, data, default=0):
        """initialize the segment tree with data"""
        self._default = default
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = self.data[i + i] + self.data[i + i + 1]

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self.data[2 * idx] + self.data[2 * idx + 1]
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = res_left + self.data[start]
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self.data[stop] + res_right
            start >>= 1
            stop >>= 1

        return res_left + res_right

# get number of gems and the number of queries
N, Q = map(int, input().split())

# get values of gems and store them in a dictionary
v1, v2, v3, v4, v5, v6 = map(int, input().split())
values = dict()
values[1], values[2], values[3], values[4], values[5], values[6] = v1, v2, v3, v4, v5, v6

# get the array of gems and store them in 6 different arrays
gems = [int(c) for c in input()]
data1 = [0]*N
data2 = [0]*N
data3 = [0]*N
data4 = [0]*N
data5 = [0]*N
data6 = [0]*N

for i in range(len(gems)):
    if gems[i] == 1:
        data1[i] = 1
    elif gems[i] == 2:
        data2[i] = 1
    elif gems[i] == 3:
        data3[i] = 1
    elif gems[i] == 4:
        data4[i] = 1
    elif gems[i] == 5:
        data5[i] = 1
    elif gems[i] == 6:
        data6[i] = 1

# create 6 segment trees for each gem
trees = dict()
trees[1], trees[2], trees[3], trees[4], trees[5], trees[6] = SegmentTree(data1), SegmentTree(data2), SegmentTree(data3), SegmentTree(data4), SegmentTree(data5), SegmentTree(data6)

# get the queries
for _ in range(Q):
    inp = list(map(int, input().split()))
    q, I = inp[0], inp[1:]
    if q == 1:
        K, P = I[0], I[1]
        # delete original Kth gem
        trees[gems[K-1]].__delitem__(K-1)
        # change value in original array
        gems[K-1] = P
        # set new Kth gem to 1
        trees[P].__setitem__(K-1, 1)
    elif q == 2:
        P, V = I[0], I[1]
        # revalue the Pth gem to value V
        values[P] = V
    elif q == 3:
        L, R = I[0], I[1]
        # get the sum of values of gems from L to R for each tree
        print(sum(trees[j].query(L-1, R) * values[j] for j in range(1, 7)))