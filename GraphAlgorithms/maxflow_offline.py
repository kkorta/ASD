# Kacper Korta rozwiązanie polega na stworzeniu superujscia do ktorego wchodza tylko 2 wiercholki, gdzie rozpatrujemy po kolei kazda pare wierzcholkow
# i wybieramy te z maksymalnym przeplywem. Zlozonosc czasowa O(V^2 * Edmonds Karp)

from zad9testy import runtests
from math import inf
import collections


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


def edmonds_karp(g, source, sink):
    n = len(g)
    parent = [-1] * n
    max_flow = 0
    graph = [i[:] for i in g]
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


def make_graph(G):
    n = 0
    for i in G:
        n = max(n, i[0], i[1])

    tab = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in G:
        u, v, w = i[0], i[1], i[2]
        tab[u][v] = w

    return tab


def maxflow(G, s):
    new_graph = make_graph(G)
    n = len(new_graph)
    max_val = 0
    for i in range(n - 1):
        if i == s:
            continue

        new_graph[i][n - 1] = inf
        for j in range(i + 1, n - 1):
            if j == s:
                continue
            new_graph[j][n - 1] = inf

            max_val = max(max_val, edmonds_karp(new_graph, s, n - 1))

            new_graph[j][n - 1] = 0
        new_graph[i][n - 1] = 0

    return max_val


runtests(maxflow)
