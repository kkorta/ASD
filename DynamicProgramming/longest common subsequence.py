def lcs(a, b):
    len1 = len(a)
    len2 = len(b)
    t = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]

    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if a[j - 1] == b[i - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    return t[len2][len1], get_solution(t, a, b, len1, len2)


def get_solution(t, a, b, len1, len2):
    index = len1
    height = len2
    solution = []
    n = t[len2][len1]
    while index > 0 and height > 0 and n > 0:
        while t[height][index - 1] == t[height][index] and index > 0:
            index -= 1
        while t[height - 1][index] == t[height][index] and height > 0:
            height -= 1

        solution.append(a[index - 1])
        n -= 1
        index -= 1
        height -= 1

    solution.reverse()
    return solution


if __name__ == '__main__':
    a = "koabcdaf"
    b = "aekoacbcf"
    print(lcs(a, b))
