from queue import Queue
from math import inf

def bfs(graph, s):
    n = len(graph)
    visited = [False] * n
    distance = [inf] * n
    distance[s] = 0
    visited[s] = True
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                distance[v] = distance[u] + 1
                q.put(v)
                visited[v] = True

    return max(distance)


def friendship_degree(friends):
    n = len(friends)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, bfs(friends, i))

    return max_val


friends = [[1, 2, 3], [0], [0], [0, 4], [3, 5], [4]]
print(friendship_degree(friends))
