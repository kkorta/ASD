def dfsHamilton(g, v, visited, S, direction):
    S.append(v)
    if len(S) < len(g):
        visited[v] = True
        if direction == 0:
            direction = 1
        else:
            direction = 0
        for e in g[v][direction]:
            if visited[e] is False:
                print(v, e)
                dfsHamilton(g, e, visited, S, direction)
        visited[v] = False
    else:
        test = False
        for u in g[v][direction]:
            if u == 0:
                test = True
            if test is True:
                return True
        S.pop()
    return None

def bipartite(g):
    n = len(g)
    q = []
    c = [0 for _ in range(n)]
    for i in range(n):
        if c[i] != 0:
            continue
        else:
            c[i] = 1
            q.append(i)
            while len(q) != 0:
                v = q[0]
                q.pop(0)
                for u in g[v]:
                    if c[u] == c[v]:
                        return False
                    elif c[u] != 0:
                        continue
                    else:
                        c[u] = -c[v]
                        q.append(u)

    return True
# G = [([1], [3]), ([2], [0]), ([3], [1]), ([0], [2])]
# g = [[1], [0], [1], [0, 1, 2]]
G1 = [[1], [2, 5, 6], [0, 3, 4], [0, 2, 4], [6, 7, 9]]
g = [([1], [2, 3, 4]), ([0], [2, 5, 6]), ([1, 5, 6], [0, 3, 4]), ([0, 2, 4], [5, 7, 8]), ([0, 2, 3], [6, 7, 9]), ([1, 2, 6], [3, 7, 8]), ([1, 2, 5], [4, 7, 9]), ([4, 6, 9], [3, 5, 8]), ([3, 5, 7], [9]), ([4, 6, 7], [8])]
visited = [False] * len(g)
S = []
print(dfsHamilton(g, 0, visited, S, 1))

print(S)
S.clear()
print(S)