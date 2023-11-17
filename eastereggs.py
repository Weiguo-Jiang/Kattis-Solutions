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

from math import sqrt

def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2


N, B, R = map(int, input().split())
blue = []
red = []
for _ in range(B):
    blue.append(tuple(map(int, input().split())))
for _ in range(R):
    red.append(tuple(map(int, input().split())))

distances = []
for i in range(B):
    distances.append([sqrt((blue[i][0] - red[j][0]) ** 2 + (blue[i][1] - red[j][1]) ** 2) for j in range(R)])

lb = 0
ub = 10**9
for i in range(50):
    mid = (lb + ub) / 2
    graph = [[] for _ in range(B)]
    for j in range(B):
        for k in range(R):
            if distances[j][k] <= mid:
                graph[j].append(k)
    match1, match2 = hopcroft_karp(graph, B, R)
    pairs = sum(1 for x in match1 if x != -1)
    if pairs <= R + B - N:
        lb = mid
    else:
        ub = mid
print(lb)