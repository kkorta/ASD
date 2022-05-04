def possibilities(T):
    m = len(T)
    n = len(T[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    def count(row, col, size):
        if row < 0 or row >= m or col < 0 or col >= n or T[row][col] is False or visited[row][col] is True:
            return size
        else:
            size += 1
            visited[row][col] = True
            tmp = size
            tmp = count(row + 1, col, tmp)
            tmp = count(row - 1, col, tmp)
            tmp = count(row, col + 1, tmp)
            tmp = count(row, col - 1, tmp)
            return tmp

    return count(0, 0, 0)


if __name__ == '__main__':
    T = [[True, False, False, True, False],
         [True, True, True, True, True],
         [True, True, True, True, False],
         [True, False, False, True, False]]

    print(possibilities(T))
