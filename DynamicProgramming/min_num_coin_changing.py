from math import inf


def min_coin(coins, s):
    n = len(coins)
    t = [[inf for _ in range(s + 1)] for _ in range(n)]

    counter = 1
    t[0][0] = 0
    for i in range(coins[0], s + 1, coins[0]):
        t[0][i] = counter
        counter += 1

    for i in range(1, n):
        t[i][0] = 0
        for j in range(s + 1):
            if coins[i] > j:
                t[i][j] = t[i - 1][j]
            else:
                t[i][j] = min(t[i - 1][j], t[i][j - coins[i]] + 1)

    if t[n - 1][s] == 0:
        return 0

    for i in t:
        print(i)

    return t[n - 1][s], get_solution(t, n, s, coins)


def get_solution(t, n, s, coins):
    index = s
    height = n - 1
    solution = []

    while index > 0 and height > 0:
        if t[height][index] == t[height - 1][index]:
            height -= 1
        else:
            index -= coins[height]
            solution.append(coins[height])

    if index > 0:
        solution.append(coins[0])

    return solution


if __name__ == '__main__':
    tab = [5, 2, 3, 1, 7]
    tab.sort()
    print(min_coin(tab, 13))