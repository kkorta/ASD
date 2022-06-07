def create_graph(I, x, y, n):
    graph = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(i + 1, n):
            if I[i][0] == I[j][1]:
                graph[j][i] = 1
            if I[i][1] == I[j][0]:
                graph[i][j] = 1

    for i in range(n):
        if I[i][0] == x:
            graph[n][i] = 1
        if I[i][1] == y:
            graph[i][n + 1] = 1

    return graph


def dfs(g, s, n):
    visited = [False] * n
    utility = [False] * n
    utility[n - 1] = True

    def dfs_visit(u):
        visited[u] = True
        for v in range(n):
            if g[u][v] == 1 and not visited[v]:
                dfs_visit(v)
                utility[u] = utility[u] or utility[v]

            if visited[v] and g[u][v] == 1 and utility[v]:
                utility[u] = True

    dfs_visit(s)
    return utility


def intuse(I, x, y):
    n = len(I)
    graph = create_graph(I, x, y, n)
    utility = dfs(graph, n, n + 2)
    result = []
    for i in range(n):
        if utility[i]:
            result.append(i)

    return result

