# Dany jest graf ważony G, oraz drzewo rozpinające T zawierające wierzchołek s. Podaj algorytm, który sprawdzi,
# czy T jest drzewem najkrótszych ścieżek od wierzchołka s.

from queue import Queue, PriorityQueue
from math import inf

def bfs(T, s):
    n = len(T)
    visited = [False] * n
    distance = [0] * n

    q = Queue()
    q.put(s)
    visited[s] = True

    while q.qsize() != 0:
        u = q.get()
        for v in T[u]:
            if visited[v[0]] is False:
                distance[v[0]] = distance[u] + v[1]
                q.put(v[0])
                visited[v[0]] = True

    return distance


def dijkstra(G, s):
    n = len(G)
    visited = [False] * n
    distance = [inf] * n
    distance[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while not pq.empty():
        dist, u = pq.get()
        for v in G[u]:
            if not visited[v[0]] and distance[v[0]] > distance[u] + v[1]:
                distance[v[0]] = distance[u] + v[1]
                pq.put((distance[v[0]], v[0]))

        visited[u] = True
    return distance


def is_shortest_path(G, T, s):
    dist1 = bfs(T, s)
    dist2 = dijkstra(G, s)
    n = len(G)
    for i in range(n):
        if dist1[i] != dist2[i]:
            return False

    return True

G = [[[1, 1], [2, 4], [3, 3]],
     [[0, 1], [2, 2], [4, 5]],
     [[0, 4], [1, 2], [4, 1], [5, 7]],
     [[0, 3], [5, 8]],
     [[1, 5], [2, 1]],
     [[2, 7],
      [3, 8]]]
T = [[[1, 1], [2, 4], [3, 3]],
     [[0, 1]],
     [[0, 4], [4, 1], [5, 7]],
     [[0, 3]],
     [[2, 1]],
     [[2, 7]]]

print(dijkstra(G, 0))
print(bfs(T, 0))
print(is_shortest_path(G, T, 0))
