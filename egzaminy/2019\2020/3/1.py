from queue import Queue


def bfs(g, s):
    q = Queue()
    n = len(g)
    visited = [False] * n
    distance = [0] * n
    q.put(s)
    visited[s] = True
    while not q.empty():
        u = q.get()
        for v in g[u]:
            if visited[v] is not True:
                visited[v] = True
                distance[v] = distance[u] + 1
                q.put(v)

    return max(distance)


def best_root(L):
    n = len(L)
    min_ = n
    index = 0
    for i in range(n):
        x = bfs(L, i)
        if x < min_:
            min_ = x
            index = i

    return index
