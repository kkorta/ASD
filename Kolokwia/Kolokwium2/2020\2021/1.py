from zad4testy import runtests


def students(i):
    return i[0] * (i[2] - i[1])


def cost(i):
    return i[3]


def select_buildings(T, p):
    n = len(T)

    parent = [-1] * n
    for i in range(n):
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    T.sort(key=lambda x: x[2])

    for i in range(n - 1):
        for j in range(i + 1, n):
            if T[i][2] < T[j][1]:
                parent[j] = i

    tab = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(p):
        if i >= cost(T[0]):
            tab[0][i] = students(T[0])

    for i in range(1, n):
        for j in range(p):
            if j >= cost(T[i]):
                if parent[i] != -1:
                    tab[i][j] = max(tab[i - 1][j], students(T[i]) + tab[parent[i]][j - cost(T[i])])
                else:
                    tab[i][j] = max(tab[i - 1][j], students(T[i]))
            else:
                tab[i][j] = tab[i - 1][j]

    return get_solution(tab, p, n, parent, T)


def get_solution(tab, p, n, parent, T):

    index = p - 1
    height = n - 1
    solution = []

    while tab[height][index] == tab[height][index - 1]:
        index -= 1

    while tab[height][index] != 0 and height > 0 and index > 0:
        if tab[height][index] == tab[height - 1][index]:
            height -= 1

        elif tab[parent[height]][index] == tab[height][index] - students(T[height]):

            solution.append(T[height][4])
            height = parent[height]

        elif tab[height][index] == tab[height][index - 1]:
            index -= 1

        elif index - cost(T[height]) >= 0:
            if tab[parent[height]][index - cost(T[height])] == tab[height][index] - students(T[height]):
                index -= cost(T[height])
                solution.append(T[height][4])
                height = parent[height]

    if index > 0 and height > 0:
        if tab[height][index] == 0:
            solution.sort()
            return solution

    elif index > 0:
        solution.append(T[height][4])

    solution.sort()

    return solution


runtests(select_buildings)
