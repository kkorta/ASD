def dfs(g, n, v, path, last):
    for e in range(last[v], n):
        if g[v][e] != 0:
            g[v][e] = 0
            g[e][v] = 0
            last[v] = e + 1
            dfs(g, n, e, path, last)

    path.insert(0, v)

def eulerian_path(g):
    n = len(g)
    path = []
    last = [0] * n
    dfs(g, n, 1, path, last)
    return path

T = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0, 1],
     [0, 1, 1, 0, 1, 1],
     [0, 0, 0, 1, 0, 1],
     [0, 1, 1, 1, 1, 0]]

