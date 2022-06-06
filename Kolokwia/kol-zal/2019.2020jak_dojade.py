from queue import PriorityQueue
from math import inf


def jak_dojade(G, P, d, a, b):
    n = len(G)
    visited = [[False for _ in range(d + 1)] for _ in range(n)]
    distance = [[inf for _ in range(d + 1)] for _ in range(n)]
    parent = [[None for _ in range(d + 1)] for _ in range(n)]
    distance[a][d] = 0
    pq = PriorityQueue()
    pq.put((0, a, d))

    while not pq.empty():
        dist, u, fuel = pq.get()
        for i in range(n):
            if G[u][i] != -1 and G[u][i] <= fuel and not visited[i][fuel]:
                if i not in P:
                    if distance[i][fuel - G[u][i]] > distance[u][fuel] + G[u][i]:
                        distance[i][fuel - G[u][i]] = distance[u][fuel] + G[u][i]
                        parent[i][fuel - G[u][i]] = (u, fuel)
                        pq.put((distance[i][fuel - G[u][i]], i, fuel - G[u][i]))
                else:
                    if distance[i][d] > distance[u][fuel] + G[u][i]:
                        distance[i][d] = distance[u][fuel] + G[u][i]
                        parent[i][d] = (u, fuel)
                        pq.put((distance[i][d], i, d))

        visited[u][fuel] = True

    index = 0
    min_val = inf
    for i in range(d + 1):
        if min_val > distance[b][i]:
            min_val = distance[b][i]
            index = i

    if min_val == inf:
        return None
    path = [b]
    i, j = parent[b][index]

    while parent[i][j] is not None:
        path.append(i)
        i, j = parent[i][j]

    path.append(a)
    return path[::-1]


G1 = [[-1, 4, 4, -1, -1],
      [-1, -1, -1, 2, -1],
      [-1, 3, -1, -1, -1],
      [-1, -1, -1, -1, 1],
      [-1, -1, -1, -1, -1]]
P1 = [0, 2]

print(jak_dojade(G1, P1, 6, 0, 4))
