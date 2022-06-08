from queue import PriorityQueue
from math import inf


def dijkstra(g, s):
    n = len(g)
    visited = [False] * n
    distance = [inf] * n
    pq = PriorityQueue()
    pq.put((0, s))
    distance[s] = 0

    while not pq.empty():
        dist, u = pq.get()
        for v in range(n):
            if not visited[v] and g[u][v] != 0:
                if distance[v] > distance[u] + g[u][v]:
                    distance[v] = distance[u] + g[u][v]
                    pq.put((distance[v], v))

        visited[u] = True

    return distance


def meeting(young, elder, a, b):
    young_dist = dijkstra(young, a)
    elder_dist = dijkstra(elder, b)
    n = len(young)
    min_val = inf
    for i in range(n):
        min_val = min(min_val, young_dist[i] + elder_dist[i])

    if min_val == inf:
        return None

    result = []
    for i in range(n):
        if young_dist[i] + elder_dist[i] == min_val:
            result.append(i)

    return result


young = [[0, 2, 10, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, 0, 0],
         [10, 0, 0, 0, 4, 0, 0],
         [0, 100, 0, 0, 7, 0, 0],
         [0, 0, 4, 7, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

elder = [[0, 2, 0, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 100, 0, 0, 7, 5, 0],
         [0, 0, 0, 7, 0, 0, 2],
         [0, 0, 0, 5, 0, 0, 4],
         [0, 0, 0, 0, 2, 4, 0]]

print(meeting(young, elder, 0, 6))

