class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def make_graph(g):
    n = len(g)
    edges = []
    for i in range(n):
        for j in g[i]:
            if [j[0], i, j[1]] not in edges:
                edges.append([i, j[0], j[1]])

    return edges


def kruskal(g):
    n = len(g)
    edges = make_graph(g)
    v = [Node(i) for i in range(n)]
    edges.sort(key=lambda x: x[2])
    result = []
    weight = 0
    for u in edges:
        i, j = u[0], u[1]
        if find(v[i]) != find(v[j]):
            result.append(u)
            union(v[i], v[j])
            weight += u[2]

    return result, weight


g = [[(1, 1)],
     [(2, 3), (4, 7)],
     [(3, 7), (6, 1)],
     [(4, 12), (6, 8), (5, 2)],
     [(5, 4)], [(7, 10), (8, 6)],
     [],
     [(8, 5)],
     []]


graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]

print(kruskal(g))
