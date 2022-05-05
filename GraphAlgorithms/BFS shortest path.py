from queue import Queue


# g-graph, s-starting point, t - target
def bfs(g, s, t):
    q = Queue()
    n = len(g)
    visited = [False] * n
    distance = [0] * n
    parents = [-1] * n
    q.put(s)
    visited[s] = True
    while q.qsize() != 0:
        u = q.get()
        for v in range(n):
            if g[u][v] != 0 and visited[v] is not True:
                visited[v] = True
                distance[v] = distance[u] + 1
                parents[v] = u
                q.put(v)

    solution = [0] * distance[t]
    index = distance[t] - 1
    while parents[t] != -1:
        solution[index] = parents[t]
        t = parents[t]
        index -= 1

    solution[0] = s

    return solution


if __name__ == '__main__':
    graph = [[0, 1, 1, 0, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 0],
             [1, 0, 0, 1, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 1, 0]]

    print(bfs(graph, 6, 3))
