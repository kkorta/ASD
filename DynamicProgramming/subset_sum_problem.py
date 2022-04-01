def ssp(num, s):
    n = len(num)
    t = [[False for _ in range(s + 1)] for _ in range(n)]
    if s == 0:
        return True

    t[0][num[0]] = True
    for i in range(n):
        t[i][0] = True

    for i in range(1, n):
        for j in range(1, s + 1):
            if num[i] > j:
                t[i][j] = t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j] or t[i - 1][j - num[i]]

    return t[n - 1][s], get_solution(num, s, t, n)


def get_solution(num, s, t, n):
    index = s
    height = n - 1
    solution = []
    while index > 0 and height > 0:
        if t[height][index] == t[height - 1][index]:
            height -= 1
        else:
            index -= num[height]
            solution.append(num[height])

    if index > 0:
        solution.append(num[0])

    return solution


if __name__ == '__main__':
    a = [2, 3, 7, 8, 10]
    print(ssp(a, 11))
