from queue import PriorityQueue
from math import inf


def check(a, b):
    nums = [0] * 10
    while a != 0:
        nums[a % 10] += 1
        a //= 10

    while b != 0:
        if nums[b % 10] > 0:
            return True

        b //= 10

    return False


def create_graph(P, n):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if check(P[i], P[j]):
                graph[i][j] = abs(P[i] - P[j])
                graph[j][i] = abs(P[i] - P[j])

    return graph


def set_source_and_target(P, n):
    max_val = 0
    min_val = inf
    max_index = 0
    min_index = 0
    for i in range(n):
        if P[i] > max_val:
            max_val = P[i]
            max_index = i
        if P[i] < min_val:
            min_val = P[i]
            min_index = i

    return min_index, max_index


def find_cost(P):
    n = len(P)
    graph = create_graph(P, n)
    s, t = set_source_and_target(P, n)
    visited = [False] * n
    distance = [inf] * n
    distance[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        dist, u = pq.get()
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
                    pq.put((dist, v))

        visited[u] = True

    if distance[t] == inf:
        return -1

    return distance[t]


P1 = [123, 890, 688, 587, 257, 246]
print(find_cost(P1))
