from queue import PriorityQueue
from math import inf


def paths(G, s, t):
    n = len(G)
    visited = [False] * n
    distance = [inf] * n
    parents = [[] for _ in range(n)]
    distance[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        dist, u = pq.get()
        for i in G[u]:
            v, cost = i[0], i[1]
            if distance[v] > distance[u] + cost:
                distance[v] = distance[u] + cost
                parents[v] = [u]
                pq.put((distance[v], v))
            elif distance[v] == distance[u] + cost:
                parents[v].append(u)

        visited[u] = True

    tab = [[0 for _ in range(n)] for _ in range(n)]

    for i in parents[t]:
        tab[t][i] = 1
        pq.put(i)

    while not pq.empty():
        u = pq.get()
        for i in parents[u]:
            tab[u][i] = 1
            pq.put(i)

    result = 0
    for i in tab:
        result += sum(i)
    return result



G = [ [(1,2),(2,4)], # sąsiedzi i wagi wierzchołka nr 0
[(0,2),(3,11),(4,3)], # sąsiedzi i wagi wierzchołka nr 1
[(0,4),(3,13)], # itd.
[(1,11),(2,13),(5,17),(6,1)],
[(1,3),(5,5)],
[(3,17),(4,5),(7,7)],
[(3,1),(7,3)],
[(5,7),(6,3)] ]

print(paths(G, 0, 7))
[[], [14], [1], [6, 7], [6], [0, 1, 28], [0], [20], [3, 3, 27, 27, 27, 27], [20], [7, 4], [28, 2, 21, 21, 21], [14], [11, 11, 11, 15, 15, 15, 10, 15, 15, 29], [9], [9, 23, 27, 27, 27, 27], [6], [14, 23], [3, 3, 23, 2], [6, 3, 3], [0], [0, 20, 28], [9, 14], [20], [0, 22, 22], [20], [9], [22, 5, 5, 5], [20], [20]]