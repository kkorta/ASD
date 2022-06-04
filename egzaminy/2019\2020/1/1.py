from queue import PriorityQueue
from math import inf


def switch(x):
    if x == 1:
        return 0
    elif x == 5:
        return 1
    else:
        return 2


def islands(G, A, B):
    n = len(G)
    visited = [[False for _ in range(3)] for _ in range(n)]
    distance = [[inf for _ in range(3)] for _ in range(n)]
    pq = PriorityQueue()
    distance[A][0] = 0
    distance[A][1] = 0
    distance[A][2] = 0
    pq.put((0, A, 0))
    while not pq.empty():
        dist, u, last = pq.get()
        curr = switch(last)
        for v in range(n):
            tmp = switch(G[u][v])
            if G[u][v] != 0 and G[u][v] != last and not visited[v][tmp]:
                if distance[v][tmp] > distance[u][curr] + G[u][v]:
                    distance[v][tmp] = distance[u][curr] + G[u][v]
                    pq.put((distance[v][tmp], v, G[u][v]))

        visited[u][curr] = True

    return min(distance[B])


G1 = [[0, 1, 0, 0, 0, 8, 0], [1, 0, 5, 0, 0, 0, 0], [0, 5, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 8], [8, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 8, 5, 0]]
G2 = [[0, 1, 0, 0, 0, 1],
      [1, 0, 5, 0, 0, 5],
      [0, 5, 0, 5, 8, 1],
      [0, 0, 5, 0, 8, 0],
      [0, 0, 8, 8, 0, 1],
      [1, 5, 1, 0, 1, 0]]
print(islands(G1, 0, 4))
print(islands(G2, 0, 3))
