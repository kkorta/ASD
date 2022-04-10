def ccp(coins, s):
    n = len(coins)
    t = [[0 for _ in range(s + 1)] for _ in range(n)]
    t[0][0] = 1

    for i in range(coins[0], s + 1, coins[0]):
        t[0][i] = 1

    for i in range(1, n):
        for j in range(s + 1):
            if j >= coins[i]:
                t[i][j] = t[i - 1][j] + t[i][j - coins[i]]
            else:
                t[i][j] = t[i - 1][j]

    return t[n - 1][s]


if __name__ == '__main__':
    tab = [2, 4, 6]
    print(ccp(tab, 10))
