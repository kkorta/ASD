def max_sum(T):
    n = len(T)
    if n == 0:
        return []
    elif n == 1:
        return [0]

    DP = [[0, -1] for _ in range(n)]
    DP[0][0] = T[0]
    DP[0][1] = 0
    DP[1][0] = max(T[0], T[1])
    if T[1] < T[0]:
        DP[1][1] = 0

    for i in range(2, n):
        DP[i][0] = max(DP[i - 2][0] + T[i], DP[i - 1][0])
        if DP[i - 2][0] + T[i] > DP[i - 1][0]:
            DP[i][1] = i - 2
        else:
            DP[i][1] = i - 1

    return get_solution(n, DP)


def get_solution(n, res):
    index = n - 1
    solution = []
    while index > 1:
        if res[index][0] == res[res[index][1]][0]:
            index = res[index][1]
        else:
            solution.append(index)
            index = res[index][1]

    solution.append(res[index][1])
    solution.reverse()
    return solution


t = [1000, 1, 300, 100000, 1, 1, 120, 37, 1, 10, 20000, 1]
print(max_sum(t))

