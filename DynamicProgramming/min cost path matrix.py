def min_cost(t):
    n = len(t)
    m = len(t[0])

    new_matrix = [[0 for _ in range(m)] for _ in range(n)]
    new_matrix[0][0] = t[0][0]

    for i in range(1, m):
        new_matrix[0][i] = new_matrix[0][i - 1] + t[0][i]

    for i in range(1, n):
        new_matrix[i][0] = new_matrix[i - 1][0] + t[i][0]

    for i in range(1, n):
        for j in range(1, m):
            new_matrix[i][j] = min(new_matrix[i - 1][j] + t[i][j], new_matrix[i][j - 1] + t[i][j])

    print(new_matrix)
    return new_matrix[n - 1][m - 1]


if __name__ == '__main__':
    tab = [[1, 3, 5, 8],
           [4, 2, 1, 7],
           [4, 3, 2, 3]]
    print(min_cost(tab))
