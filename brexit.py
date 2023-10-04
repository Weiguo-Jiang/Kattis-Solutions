#
# BEGIN-HEADER
#
# Name: Weiguo Jiang
#
# Student-ID: 1670913
#
# List any resources you used below (eg. urls, name of the algorithm from our code archive).
# Remember, you are permitted to get help with general concepts about algorithms
# and problem-solving, but you are not permitted to hunt down solutions to
# these particular problems!
#
# PyRival Repo: https://github.com/cheran-senthil/PyRival
#
# By submitting this code, you are agreeing that you have solved in accordance
# with the collaboration policy in CMPUT 303/403.
#
# END-HEADER
#

from collections import deque
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

C, P, X, L = list(map(int, input().split()))
if X == L:
    print("leave")
else:
    d = dict()
    for i in range(C):
        d[i] = set()
    for i in range(P):
        c1, c2 = list(map(int, input().split()))
        c1 -= 1
        c2 -= 1
        d[c1].add(c2)
        d[c2].add(c1)
    half = list()
    for i in range(C):
        half.append(len(d[i]) // 2)

    q = deque()
    q.append(L - 1)
    visited = set()
    visited.add(L - 1)

    while q:
        p = q.popleft()
        for partner in d[p]:
            d[partner].remove(p)
            if partner not in visited and len(d[partner]) <= half[partner]:
                q.append(partner)
                visited.add(partner)
        del d[p]

    if X - 1 in d:
        print("stay")
    else:
        print("leave")