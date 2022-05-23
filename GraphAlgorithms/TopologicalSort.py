def dfs(g, v, sorted_g, visited):
    visited[v] = True
    for e in g[v]:
        if visited[e] is False:
            dfs(g, e, sorted_g, visited)

    sorted_g.insert(0, v)


def topological_sort(g):
    n = len(g)
    visited = [False] * n
    path = []
    for e in range(n):
        if visited[e] is False:
            dfs(g, e, path, visited)

    return path


def dfs_matrix(g, n, v, sorted_g, visited):
    visited[v] = True
    for e in range(n):
        if visited[e] is False and g[v][e] != 0:
            dfs_matrix(g, n, e, sorted_g, visited)

    sorted_g.insert(0, v)


def topological_sort_matrix(g):
    n = len(g)
    visited = [False] * n
    path = []
    for e in range(n):
        if visited[e] is False:
            dfs_matrix(g, n, e, path, visited)

    return path


G = [[1,2,6],[],[3,1],[4,5],[],[],[3]]
g1 = [[0, 1, 1, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0]]

T = [[0, 1, 0, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]]
print(topological_sort(G))
print(topological_sort_matrix(g1))
