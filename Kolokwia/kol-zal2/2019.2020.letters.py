from queue import PriorityQueue
from math import inf


def create_graph(E, n):
    graph = [[] for _ in range(n)]
    for i in E:
        graph[i[0]].append([i[1], i[2]])
        graph[i[1]].append([i[0], i[2]])

    return graph


def letters(G, W):
    n = len(G[0])
    m = len(W)
    pq = PriorityQueue()
    graph = create_graph(G[1], n)
    for i in range(n):
        if G[0][i] == W[0]:
            pq.put((0, i, 1))

    min_val = inf
    while not pq.empty():
        dist, u, nr = pq.get()
        if nr < m:
            for i in graph[u]:
                if G[0][i[0]] == W[nr]:
                    pq.put((dist + i[1], i[0], nr + 1))
        else:
            min_val = min(min_val, dist)

    if min_val == inf:
        return -1

    return min_val


L3 = ['k', 'k', 'k', 'u', 'u', 'u', 't', 't', 'a', 's', 's']
E3 = [(0, 1, 3), (0, 4, 3), (0, 6, 2), (0, 8, 1), (1, 3, 2), (1, 5, 3), (1, 7, 4), (2, 3, 1), (2, 6, 4), (2, 9, 5),
      (3, 5, 2), (3, 7, 2), (3, 6, 5), (4, 8, 8), (5, 6, 1), (6, 7, 5), (7, 8, 2), (8, 10, 2), (8, 9, 3)]
G3 = (L3, E3)
print(letters(G3, 'kutas'))