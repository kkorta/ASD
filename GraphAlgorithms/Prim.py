from queue import PriorityQueue
from math import inf


def prim(g):
    n = len(g)
    visited = [False] * n
    distance = [inf] * n
    parent = [None] * n
    pq = PriorityQueue()
    visited[0] = True
    distance[0] = 0
    pq.put((0, 0))
    while not pq.empty():
        dist, u = pq.get()
        visited[u] = True
        for i in range(n):
            if g[u][i] != 0 and visited[i] is False and distance[i] > g[u][i]:
                parent[i] = u
                distance[i] = g[u][i]
                pq.put((g[u][i], i))

    result = []
    weight = 0
    for i in range(1, n):
        result.append((parent[i], i, distance[i]))
        weight += distance[i]
    return result, weight


g = [[(1, 1)],
     [(2, 3), (4, 7)],
     [(3, 7), (6, 1)],
     [(4, 12), (6, 8), (5, 2)],
     [(5, 4)], [(7, 10), (8, 6)],
     [],
     [(8, 5)],
     []]

g1 = [[0, 1, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 3, 0, 7, 0, 0, 0, 0],
      [0, 3, 0, 7, 0, 0, 1, 0, 0],
      [0, 0, 7, 0, 12, 2, 8, 0, 0],
      [0, 7, 0, 12, 0, 4, 0, 10, 6],
      [0, 0, 0, 2, 4, 0, 0, 0, 0],
      [0, 0, 1, 8, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 10, 0, 0, 0, 5],
      [0, 0, 0, 0, 6, 0, 0, 5, 0]]

print(prim(g1))