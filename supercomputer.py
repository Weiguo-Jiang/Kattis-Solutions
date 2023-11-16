class SegmentTree:
    def __init__(self, data, default=0, func=sum):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func([self.data[i + i], self.data[i + i + 1]])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func([self.data[2 * idx], self.data[2 * idx + 1]])
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
                res_left = self._func([res_left, self.data[start]])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func([self.data[stop], res_right])
            start >>= 1
            stop >>= 1

        return self._func([res_left, res_right])

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

N, K = map(int, input().split())
data = [0] * N
segment_tree = SegmentTree(data)
for _ in range(K):
    query = input().split()
    if len(query) == 2:
        i = int(query[1]) - 1
        segment_tree.__setitem__(i, 1- segment_tree.__getitem__(i))
    else:
        l, r = map(int, query[1:])
        print(segment_tree.query(l-1, r))