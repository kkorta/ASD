from _collections import deque


def BFS(G, s):
    visited = [False for _ in range(len(G))]
    Q = deque([])
    visited[s] = True
    Q.append(s)
    n = len(G)
    distance = [0 for _ in range(n)]
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if visited[u] == False:
                distance[u] = distance[v] + 1
                visited[u] = True
                Q.append(u)
    return distance


def enlarge(G, s, t):
    t1 = BFS(G, s)
    if t1[t] == 0:
        return None
    t2 = BFS(G, t)
    max_steps = t1[t]
    n = len(G)
    index = 0
    count = 0
    p = [-1] * (max_steps + 1)
    for i in range(max_steps + 1):
        for j in range(n):
            if t1[j] == i and t1[j] + t2[j] == max_steps:
                count += 1
                index = j

        if count == 1:
            p[i] = index

        count = 0

    for i in range(max_steps):
        if p[i] >= 0 and p[i + 1] >= 0:
            return p[i], p[i + 1]

    return None


if __name__ == '__main__':
    g = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    g1 = [[1, 10], [0, 2, 9], [1, 3], [2, 4], [3, 5, 8], [4, 6, 8], [5, 7], [6, 8], [4, 5, 7, 9], [1, 8, 10], [0, 9]]
    G = [[1, 2],
         [0, 2],
         [0, 1]]
    G2 = [[1, 4],  # 0
          [0, 2],  # 1
          [1, 3],  # 2
          [2, 5],  # 3
          [0, 5],  # 4
          [4, 3]]  # 5
    s2 = 0
    t2 = 3
    r2 = None

    s3 = 0
    t3 = 2
    r3 = [(0, 1), (1, 2)]
    G4 = [[1, 4, 3],  # 0
          [0, 2],  # 1
          [1, 3],  # 2
          [2, 5, 0],  # 3
          [0, 5],  # 4
          [4, 3]]  # 5
    s4 = 0
    t4 = 2
    r4 = None


    G5 = [[1,2], [0,2], [0,1,3], [2,4], [3]]

    print(enlarge(G5, 0, 4))

