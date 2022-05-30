from queue import PriorityQueue
from math import *

def tourist_guide(g, s, t, p):
    n = len(g)
    visited = [False] * n
    parent = [None] * n
    distance = [0] * n
    distance[s] = inf
    pq = PriorityQueue()
    pq.put((-inf, s))

    while not pq.empty():
        dist, u = pq.get()
        for i in range(n):
            if g[u][i] != 0 and not visited[i]:
                if distance[i] < min(distance[u], g[u][i]):
                    distance[i] = min(distance[u], g[u][i])
                    parent[i] = u
                    pq.put((-distance[i], i))

        visited[u] = True

    path = []
    index = t
    while parent[index] is not None:
        path.append(parent[index])
        index = parent[index]

    path.reverse()

    return distance[t], path, ceil(p / distance[t])


graph = [[0, 20, 10, 0, 0, 0],
         [20, 0, 25, 80, 0, 0],
         [10, 25, 0, 19, 30, 0],
         [0, 80, 19, 0, 4, 10],
         [0, 0, 30, 4, 0, 37],
         [0, 0, 0, 10, 39, 0]]

g1 = [[0, 10, 10, 0, 0, 0],
      [10, 0, 0, 8, 0, 5],
      [10, 0, 0, 0, 9, 0],
      [0, 8, 0, 0, 0, 6],
      [0, 0, 9, 0, 0, 8],
      [0, 5, 0, 6, 8, 0]]
print(tourist_guide(graph, 0, 5, 10))
print(tourist_guide(g1, 0, 5, 10))

