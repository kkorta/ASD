from queue import PriorityQueue
from math import inf


def gas_station_problem(graph, prices, s, t, d):
    n = len(graph)
    visited = [False] * n
    cost = [[inf for _ in range(d + 1)] for _ in range(n)]
    cost[s][d] = 0
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        dist, u = pq.get()
        for v in range(n):
            if graph[u][v] != 0 and graph[u][v] <= d and not visited[v]:
                cost[v][0] = cost[u][graph[u][v]]
                for i in range(1, d + 1):
                    if i + graph[u][v] <= d:
                        cost[v][i] = min(cost[v][i - 1] + prices[v], cost[u][i + graph[u][v]])
                    else:
                        cost[v][i] = cost[v][i - 1] + prices[v]

                pq.put((dist + graph[u][v], v))

        visited[u] = True

    for i in cost:
        print(i)
    return min(cost[t])


tab = [[0, 8, 5, 0, 0],
       [8, 0, 0, 4, 0],
       [5, 0, 0, 3, 0],
       [0, 4, 3, 0, 1],
       [0, 0, 0, 1, 0]]
price = [0, 1, 100, 10, 1]

print(gas_station_problem(tab, price, 0, 4, 10))
