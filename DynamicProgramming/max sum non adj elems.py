def max_sum(T):
    n = len(T)

    if n == 0:
        return 0
    elif n == 1:
        return T[0]

    DP = [0] * n
    DP[0] = T[0]
    DP[1] = max(T[0], T[1])

    for i in range(2, n):
        DP[i] = max(DP[i - 2] + T[i], DP[i - 1])

    return DP[n - 1]


if __name__ == '__main__':
    t = [1000, 1, 300, 100000]
    print(max_sum(t))
