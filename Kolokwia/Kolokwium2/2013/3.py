def captain_problem(T, k):
    m = len(T)
    n = len(T[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    def captain_visit(row, col):
        if row < 0 or row >= m or col < 0 or col >= n or T[row][col] > k or visited[row][col] == True:
            return
        else:
            visited[row][col] = True
            captain_visit(row + 1, col)
            captain_visit(row - 1, col)
            captain_visit(row, col + 1)
            captain_visit(row, col + 1)
            return

    captain_visit(0, 0)
    return visited[m - 1][n - 1]


if __name__ == '__main__':
    tab = [[1, 5, 5, 1, 6],
           [2, 3, 4, 1, 3],
           [1, 1, 1, 1, 10],
           [1, 15, 15, 1, 6]]

    print(captain_problem(tab, 4))

