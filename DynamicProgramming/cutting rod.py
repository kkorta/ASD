def cutting_rod(V, L, length):
    n = len(V)
    t = [[0 for _ in range(length + 1)] for _ in range(n)]

    for i in range(L[0], length + 1, L[0]):
        t[0][i] = t[0][i - L[0]] + V[0]

    for i in range(1, n):
        for j in range(1, length + 1):
            if j >= L[i]:
                t[i][j] = max(t[i - 1][j], t[i][j - L[i]] + V[i])
            else:
                t[i][j] = t[i - 1][j]
  
    return t[n - 1][length], get_solution(L, length, n, t)


def get_solution(L, index, n, t):
    height = n - 1
    solution = []
    while t[height][index] != 0 and height > 0 and index > 0:
        if t[height][index] == t[height - 1][index]:
            height -= 1
        else:
            solution.append(L[height])
            index -= L[height]

    if t[height][index] != 0:
        solution.append(L[height])

    return solution


if __name__ == '__main__':
    length = 5 #length of the rod we want to cut
    V = [2, 5, 7, 8] #values for the length in array L
    L = [1, 2, 3, 4] #length

    V1 = [2, 3, 6, 7, 9]
    L1 = [2, 3, 4, 6, 7]
    print(cutting_rod(V, L, length))
    print(cutting_rod(V1, L1, 14))
