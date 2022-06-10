from math import inf


import copy, collections

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


def floyd_warshall(g):
    n = len(g)
    distance = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if g[i][j] != 0:
                distance[i][j] = g[i][j]
            elif i == j:
                distance[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance


def BlueAndGreen(T, K, D):
    n = len(T)
    distance = floyd_warshall(T)

    new_graph = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(i + 1, n):
            if distance[i][j] >= D:
                if K[i] == 'B' and K[j] == 'G':
                    new_graph[i][j] = 1
                elif K[i] == 'G' and K[j] == 'B':
                    new_graph[j][i] = 1

    for i in range(n):
        if K[i] == 'B':
            new_graph[n][i] = 1
        else:
            new_graph[i][n + 1] = 1

    return edmonds_karp(new_graph, n, n + 1)
