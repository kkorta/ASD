def optimal_result(T):
    n = len(T)
    tab = [[[0, 0] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        tab[i][i][0] = T[i]

    for i in range(1, n):
        index = i
        height = 0
        for j in range(i, n):
            if tab[height + 1][index][1] + T[height] > tab[height][index - 1][1] + T[index]:
                tab[height][index][0] = tab[height + 1][index][1] + T[height]
                tab[height][index][1] = tab[height + 1][index][0]

            else:
                tab[height][index][0] = tab[height][index - 1][1] + T[index]
                tab[height][index][1] = tab[height][index - 1][0]

            height += 1
            index += 1

    return tab[0][n - 1][0]


if __name__ == '__main__':

    t = [3, 9, 1, 2]
    print(optimal_result(t))
