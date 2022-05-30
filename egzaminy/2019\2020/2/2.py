from zad8testy import runtests
from math import *


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
        return False
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return True


def length(a, b):
    return ceil(sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))


def make_graph(A, n):
    graph = []
    for i in range(n):
        for j in range(i + 1, n):
            graph.append([i, j, length(A[i], A[j])])

    graph.sort(key=lambda x: x[2])
    return graph


def kruskal(E, n, m, i):
    v = [Node(i) for i in range(n)]
    result = []
    size = 0
    for j in range(i, m):
        if size + 1 >= n:
            break

        h, k = E[j][0], E[j][1]
        if union(v[h], v[k]):
            size += 1
            result.append(E[j])

    if size + 1 != n:
        return inf

    return result[size - 1][2] - result[0][2]


def highway(A):
    n = len(A)
    E = make_graph(A, n)
    m = len(E)
    min_ = inf
    for i in range(m - n + 2):
        min_ = min(min_, kruskal(E, n, m, i))

    return min_


runtests(highway)
