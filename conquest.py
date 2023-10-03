import heapq
import os
import sys
from io import BytesIO, IOBase

_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

N, M = map(int, input().split())
d = dict()
for i in range(1, N+1):
    d[i] = []

for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

size = dict()
for i in range(1, N+1):
    size[i] = int(input())

conquered = set()
conquered.add(1)
army_size = size[1]
l = []
for i in d[1]:
    heapq.heappush(l, (size[i], i))
heapq.heapify(l)

while l:
    island_size, cur_island = heapq.heappop(l)
    if cur_island in conquered:
        continue

    if army_size <= island_size:
        break
    conquered.add(cur_island)
    army_size += island_size
    for i in d[cur_island]:
        if i not in conquered:
            heapq.heappush(l, (size[i], i))
print(army_size)