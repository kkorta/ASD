def check(a, b, k):
    m = 10 ** k
    return a % m == b // m


def create_graph(L, k):
    n = len(L)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if check(L[i], L[j], k):
                graph[i].append(j)
            if check(L[j], L[i], k):
                graph[j].append(i)

    return graph


def dfs(L, g, v, sorted_g, visited):
    visited[v] = True
    for e in g[v]:
        if visited[e] is False:
            dfs(L, g, e, sorted_g, visited)

    sorted_g.insert(0, L[v])


def topological_sort(L, g, k):
    n = len(g)
    visited = [False] * n
    path = []
    for e in range(n):
        if visited[e] is False:
            dfs(L, g, e, path, visited)

    for i in range(1, n):
        if not check(path[i - 1], path[i], k):
            return None

    return path


def order(L, k):
    return topological_sort(L, create_graph(L, k), k)
