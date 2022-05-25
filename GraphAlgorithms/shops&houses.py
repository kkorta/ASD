from queue import PriorityQueue
from math import inf


def dijkstra(G, s, distance):
    n = len(G)
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, s))
    while not pq.empty():
        dist, u = pq.get()

        for i in G[u]:
            v, weight = i[0], i[1]
            if not visited[v]:
                if distance[v] > distance[u] + weight:
                    distance[v] = distance[u] + weight
                    pq.put((distance[v], v))
        visited[u] = True

    return distance


def shops_and_houses(shops, g):
    n = len(g)
    distance = [inf] * n
    for i in shops:
        distance[i] = 0
        dijkstra(g, i, distance)

    return distance


if __name__ == '__main__':
    shops = [0, 3, 7]
    g = [[[1, 5], [2, 4]],
         [[0, 5], [3, 3]],
         [[0, 4], [3, 1]],
         [[1, 3], [2, 1], [4, 9]],
         [[3, 9], [5, 3]],
         [[2, 6], [4, 3], [6, 1]],
         [[5, 1], [7, 2]],
         [[6, 2]]]
    print(shops_and_houses(shops, g))



