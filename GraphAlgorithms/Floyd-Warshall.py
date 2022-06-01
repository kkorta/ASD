from math import inf


def floyd_warshall(g):
    n = len(g)
    distance = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if g[i][j] != 0:
                distance[i][j] = g[i][j]
                parent[i][j] = i
            elif i == j:
                distance[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    print(k, i, j)
                    distance[i][j] = distance[i][k] + distance[k][j]
                    parent[i][j] = parent[k][j]

    return distance


def get_path(parent, s, t):
    path = [t]
    v = parent[s][t]
    while v != s:
        path.append(v)
        v = parent[s][v]
    path.append(s)
    return path[::-1]


T = [[0, 4, 0, 0],
     [4, 0, 4, 0],
     [0, 4, 0, 4],
     [0, 0, 4, 0]]

print(floyd_warshall(T))
