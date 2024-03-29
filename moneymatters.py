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

n, m = map(int, input().split())
debts = dict()
for i in range(n):
    debts[i] = int(input())

relationships = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a not in relationships:
        relationships[a] = []
    if b not in relationships:
        relationships[b] = []
    relationships[a].append(b)
    relationships[b].append(a)

connected_components = []
visited = set()
while len(visited) < n:
    component = []
    l = []
    for i in range(n):
        if i not in visited:
            component.append(i)
            visited.add(i)
            l.append(i)
            break

    while l:
        cur = l.pop()
        for i in relationships[cur]:
            if i not in visited:
                component.append(i)
                visited.add(i)
                l.append(i)
    connected_components.append(component)

for component in connected_components:
    balance = 0
    for i in component:
        balance += debts[i]
    if balance != 0:
        print("IMPOSSIBLE")
        exit()
print("POSSIBLE")