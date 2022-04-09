def lcs(a, b):
    len1 = len(a)
    len2 = len(b)
    t = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]

    for i in range(len2):
        for j in range(len1):
            if b[i] == a[j]:
                t[i + 1][j + 1] = t[i][j] + 1

    maxym = 0
    max_j = 0
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if t[i][j] > maxym:
                maxym = t[i][j]
                max_j = j

    return maxym, get_solution(a, maxym, max_j)


def get_solution(a, steps, j):
    solution = []
    for i in range(steps):
        solution.append(a[j - 1])
        j -= 1

    solution.reverse()
    return solution


if __name__ == '__main__':
    a = [1, 2, 3, 4, 6]
    b = [2, 1, 2, 3, 4, 5, 6, 7]
    a1 = "abcdf"
    b1 = "kaabcg"
    print(lcs(a, b))
    print(lcs(a1, b1))
