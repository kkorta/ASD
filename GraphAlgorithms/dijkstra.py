from math import inf
from queue import PriorityQueue


def dijkstra(g, s):
    n = len(g)
    visited = [False] * n
    distance = [inf] * n
    parent = [None] * n
    pq = PriorityQueue()
    distance[s] = 0
    pq.put((0, s))
    while not pq.empty():
        dist, u = pq.get()

        for v in range(n):
            if not visited[v] and g[u][v] != 0:
                if distance[v] > distance[u] + g[u][v]:
                    distance[v] = distance[u] + g[u][v]
                    parent[v] = u
                    pq.put((distance[v], v))

        visited[u] = True

    return parent, distance


graph = [[0, 5, 0, 0, 0, 2],
         [5, 0, 5, 0, 0, 0],
         [0, 5, 0, 3, 0, 10],
         [0, 0, 3, 0, 2, 4],
         [0, 0, 0, 2, 0, 2],
         [2, 0, 10, 4, 2, 0]]
print(dijkstra(graph, 0))
