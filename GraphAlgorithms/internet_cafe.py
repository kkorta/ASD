from collections import deque
from math import inf


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = deque()
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


def edmonds_karp(graph, source, sink, k, a):
    n = len(graph)
    parent = [-1] * n
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

    if max_flow != k:
        print("Solution doesn't exist")
        return None

    result = []
    for i in range(k, k + k):
        for j in range(a):
            if graph[i][j] == 1:
                result.append(j)
                break

    return result


def create_graph(apps, available, k):
    a = len(apps)
    n = a + k + 2
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(k):
        for j in available[i]:
            graph[i][j + k] = 1

    for i in range(k, k + k):
        graph[i][n - 1] = 1

    for j in range(a):
        graph[n - 2][j] = apps[j]

    return graph


def internet_cafe(apps, available, k):
    if sum(apps) != k:
        print("Solution doesn't exist")
        return None
    a = len(apps)
    graph = create_graph(apps, available, k)
    n = a + k + 2
    return edmonds_karp(graph, n - 2, n - 1, k, a)


applications = [2, 0, 1, 1]
available_on_computer = [[0, 1, 2, 3], [1, 2], [3], [3]]
print(internet_cafe(applications, available_on_computer, 4))


