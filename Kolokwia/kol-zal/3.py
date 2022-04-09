from math import inf

def iamlate(T, V, q, l):
    n = len(T)

    tab = [[[inf, -1, -1] for _ in range(q + 1)] for _ in range(n)]
    tab[0][min(q, V[0])][0] = 1

    for i in range(1, n):
        for j in range(q + 1):
            if j + T[i] - T[i - 1] <= q:
                if tab[i - 1][j + T[i] - T[i - 1]][0] != inf:
                    if tab[i - 1][j + T[i] - T[i - 1]][0] < tab[i][j][0]:
                        tab[i][j][0], tab[i][j][1], tab[i][j][2] = tab[i - 1][j + T[i] - T[i - 1]][0], i - 1, j + T[i] - T[i - 1]

                    if j + V[i] >= q:
                        if tab[i][q][0] > tab[i][j][0] + 1:
                            tab[i][q][0], tab[i][q][1], tab[i][q][2] = tab[i][j][0] + 1, i, j
                    else:
                        if tab[i][j + V[i]][0] > tab[i][j][0] + 1:
                            tab[i][j + V[i]][0], tab[i][j + V[i]][1], tab[i][j + V[i]][2] = tab[i][j][0] + 1, i, j
    index = 0
    minim = inf
    for i in range(q + 1):
        if tab[n - 1][i][0] <= minim and T[n - 1] + i >= l:
            minim = tab[n - 1][i][0]
            index = i

    if minim == inf or index + T[n - 1] < l:
        return []

    return get_soultion(tab, n - 1, index), minim


def get_soultion(tab, height, index):
    solution = []
    fueled = False
    while tab[height][index][1] != -1 and tab[height][index][2] != -1:

        if height == tab[height][index][1]:
            height, index = tab[height][index][1], tab[height][index][2]
            fueled = True
        else:
            if fueled:
                solution.append(height)
            height, index = tab[height][index][1], tab[height][index][2]

            fueled = False

    solution.append(0)
    solution.reverse()
    return solution


if __name__ == '__main__':
    V =[2, 3, 1, 5, 3]
    T =[0, 2, 3, 4, 5]
    l = 8
    q = 3
    T1 = [0, 5, 10]
    V1 = [10, 5, 20]
    q1 = 100
    l1 = 35
    print(iamlate(T, V, q, l))
    print(iamlate(T1, V1, q1, l1))
