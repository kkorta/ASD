def students(i):
    return i[0] * (i[2] - i[1])

def cost(i):
    return i[3]


def select_buildings(T, p):
    n = len(T)
    parent = [-1] * n
    T.sort(key=lambda x: x[2])
    for i in range(n - 1):
        for j in range(i + 1, n):
            if T[i][2] <= T[j][1]:
                parent[j] = i

    tab = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(p):
        if i >= cost(T[0]):
            tab[0][i] = students(T[0])

    for i in range(1, n):
        for j in range(p):
            if j >= cost(T[i]):
                tab[i][j] = max(tab[i - 1][j], students(T[i]) + tab[parent[i]][j - cost(T[i])])
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

            solution.append(height)
            height = parent[height]

        elif tab[height][index] == tab[height][index - 1]:
            index -= 1

        elif index - cost(T[height]) >= 0:
            if tab[height][index] == tab[height][index - cost(T[height])] + students(T[height]):
                index -= cost(T[height])
                solution.append(height)


    if index > 0:
        solution.append(height)

    solution.reverse()

    return solution


if __name__ == '__main__':
    P1 = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
    R1 = [0, 2]
    C1 = 6

    P2 = [(8, 2, 6, 2), (9, 4, 8, 5), (9, 8, 9, 2), (3, 10, 15, 1)]
    R2 = [0, 2, 3]
    C2 = 7

    P3 = [(7, 23, 24, 1), (2, 10, 14, 3), (7, 17, 22, 1), (9, 20, 22, 2), (4, 19, 22, 8), (2, 2, 6, 1)]
    R3 = [0, 1, 2, 5]
    C3 = 10

    P4 = [(1, 8, 12, 5), (4, 7, 8, 2), (3, 2, 3, 6), (9, 7, 8, 5), (8, 21, 22, 8), (5, 4, 7, 10), (1, 21, 24, 10),
           (7, 14, 16, 1)]
    R4 = [0, 2, 4, 5, 7]#zła odpowiedź? pokazuje 44 a mozna zdobyc 50
    C4 = 32

    print(select_buildings(P1, C1))
    print(select_buildings(P2, C2))
    print(select_buildings(P3, C3))
    print(select_buildings(P4, C4))