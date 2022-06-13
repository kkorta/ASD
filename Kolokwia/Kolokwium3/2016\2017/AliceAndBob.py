from math import inf
from queue import PriorityQueue


def switch(x):
    if x == 1:
        return 0

    return 1


def dijkstra(g, s, t, turn):
    n = len(g)
    distance = [[inf, inf] for _ in range(n)]
    parent = [[None, None] for _ in range(n)]
    distance[s][switch(turn)] = 0
    pq = PriorityQueue()
    pq.put((0, s, turn))
    while not pq.empty():
        dist, u, tur = pq.get()
        for v in range(n):
            if g[u][v] != 0 and distance[v][turn] == inf:
                if tur == 0 and distance[v][0] > distance[u][1]:
                    distance[v][0] = distance[u][1]
                    parent[v][0] = u
                    pq.put((distance[v][0], v, 1))
                elif tur == 1 and distance[v][1] > distance[u][0] + g[u][v]:
                    distance[v][1] = distance[u][0] + g[u][v]
                    parent[v][1] = u
                    pq.put((distance[v][1], v, 0))

    return parent, distance[t]


def get_path(distance, parent, t):
    if distance[0] > distance[1]:
        turn = 1
    else:
        turn = 0

    path = []
    while t is not None:
        path.append(t)
        t = parent[t][turn]
        turn = switch(turn)

    path.reverse()
    return path


def AliceAndBob(g, s, t):
    a_parent, a_distance = dijkstra(g, s, t, 1)
    b_parent, b_distance = dijkstra(g, s, t, 0)
    if min(a_distance) == min(b_distance) == inf:
        return []

    if min(a_distance) > min(b_distance):
        return "Bob", get_path(b_distance, b_parent, t)

    return "Alice", get_path(a_distance, a_parent, t)


G = [[0, 8, 15, 0, 0, 12, 0, 0, 0, 0, 10, 0, 30],
     [0, 0, 4, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 10, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0],
     [0, 0, 0, 18, 0, 0, 20, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 11, 0, 0, 8, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 25, 0, 0],
     [0, 0, 0, 0, 0, 19, 0, 10, 0, 0, 0, 25, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0]]


print(AliceAndBob(G, 0, 7))
print(AliceAndBob(G, 0, 5))
print(AliceAndBob(G, 0, 11))
print(AliceAndBob(G, 0, 8))
print(AliceAndBob(G, 1, 0))
print(AliceAndBob(G, 9, 2))