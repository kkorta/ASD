def dfs(g, n, v, path):
    for e in range(n):
        if g[v][e] != 0:
            g[v][e] = 0
            g[e][v] = 0
            dfs(g, n, e, path)

    path.insert(0, v)

def eulerian_path(g):
    n = len(g)
    path = []
    dfs(g, n, 0, path)
    return path

T = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0, 1],
     [0, 1, 1, 0, 1, 1],
     [0, 0, 0, 1, 0, 1],
     [0, 1, 1, 1, 1, 0]]

print(eulerian_path(T))