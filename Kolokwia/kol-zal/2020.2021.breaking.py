def dfs(g, x):
    n = len(g)
    visited = [False] * n

    def dfs_visit(u):
        visited[u] = True
        for v in range(n):
            if g[u][v] != 0 and not visited[v] and v != x:
                dfs_visit(v)

    count = 1
    for i in range(n):
        if i != x and not visited[i]:
            dfs_visit(i)
            count += 1

    return count


def breaking(G):
    n = len(G)
    max_val = 0
    index = 0
    for i in range(n):
        curr = dfs(G, i)
        if curr > max_val:
            max_val = curr
            index = i

    if max_val == 2:
        return None

    return index


