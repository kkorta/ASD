from queue import PriorityQueue
from math import inf

def islands(G, A, B):
    n = len(G)
    visited = [False] * n
    distance = [inf] * n
    pq = PriorityQueue()
    visited[A] = True
    distance[A] = 0
    pq.put((0, A, 0))
    while not pq.empty():
        dist, u, last = pq.get()
        for v in range(n):
            if G[u][v] != 0 and G[u][v] != last and not visited[v]:
                if distance[v] > distance[u] + G[u][v]:
                    distance[v] = distance[u] + G[u][v]
                    pq.put((distance[v], v, G[u][v]))

        visited[u] = True

    if distance[B] == inf:
        return None

    return distance[B]