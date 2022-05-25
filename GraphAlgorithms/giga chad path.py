# giga chad path is shortest path in weighted graph where number of edges the path contains is minimal

from queue import PriorityQueue
from math import inf


def giga_chad_path(G, s, t):
    n = len(G)
    visited = [False] * n
    distance = [inf] * n
    parents = [-1] * n
    distance[s] = 0
    edges = [inf] * n
    edges[s] = 0
    pq = PriorityQueue()
    pq.put((0, s, 0))

    while not pq.empty():
        dist, u, edge = pq.get()
        for i in range(n):
            if not visited[i] and G[u][i] != 0:
                if distance[i] >= distance[u] + G[u][i]:
                    if edges[i] > edges[u] + 1:
                        edges[i] = edges[u] + 1
                        parents[i] = u

                    distance[i] = distance[u] + G[u][i]
                    pq.put((distance[i], i, edges[i]))
        visited[u] = True

    result = []
    result.append(t)
    while parents[t] != -1:
        result.append(parents[t])
        t = parents[t]

    result.reverse()

    return result #distance, edges, parents, 


g = [[0, 2, 0, 0, 5, 0],
     [2, 0, 3, 0, 0, 0],
     [0, 3, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 3],
     [5, 0, 0, 1, 0, 0],
     [0, 0, 0, 3, 0, 0]]

print(giga_chad_path(g, 0, 5))

g1 = [[0, 3, 0, 0, 0, 0, 8, 0, 0],
      [3, 0, 4, 0, 0, 0, 0, 0, 0],
      [0, 4, 0, 6, 0, 0, 0, 10, 0],
      [0, 0, 6, 0, 2, 0, 5, 0, 0],
      [0, 0, 0, 2, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 2],
      [8, 0, 0, 5, 0, 0, 0, 0, 0],
      [0, 0, 10, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 2, 0, 1, 0]]

print(giga_chad_path(g1, 0, 8))