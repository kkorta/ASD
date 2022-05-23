def make_graph(T):
    n = len(T)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if T[i][j] == 2:
                graph[j][i] = 1

    return graph


def dfs_matrix(g, n, v, sorted_g, visited):
    visited[v] = True
    for e in range(n):
        if visited[e] is False and g[v][e] != 0:
            dfs_matrix(g, n, e, sorted_g, visited)

    sorted_g.insert(0, v)


def topological_sort_matrix(g):
    n = len(g)
    visited = [False] * n
    path = []
    for e in range(n):
        if visited[e] is False:
            dfs_matrix(g, n, e, path, visited)

    return path


def Tasks(T):
    return topological_sort_matrix(make_graph(T))


TESTS = [

    ([[0, 2, 1, 1], [1, 0, 1, 1], [2, 2, 0, 1], [2, 2, 2, 0]], [1, 0, 2, 3]),
    ([[0, 0, 2, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [2, 0, 0, 0, 0]], [2, 1, 0, 3, 4]),
    ([[0, 0, 0, 2], [0, 0, 1, 2], [0, 2, 0, 0], [1, 1, 0, 0]], [3, 1, 2, 0])

]


def runtests(f):
    OK = True
    for (A, R) in TESTS:
        y = f(A)

        try:
            print("----------------------")
            print("A =", A)
            print("otrzymany wynik  =", y)

            n = len(A)
            for j in range(n):
                for i in range(j):
                    if A[y[i]][y[j]] == 2:
                        print("Blad: Zadanie %d poprzedza zadanie %d" % (y[i], y[j]))
                        OK = False

            print("----------------------")

        except TypeError:
            print("Bledny typ zwracanego wyniku")
            OK = False

    if OK:
        print("OK!")
    else:
        print("Bledy!")


runtests(Tasks)