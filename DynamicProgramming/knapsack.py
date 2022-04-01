def knapsack(W, P, weight):
    n = len(W)
    T = [[0 for _ in range(weight + 1)] for _ in range(n)]
    for i in range(W[0], weight + 1):
        T[0][i] = P[0]

    for i in range(1, n):
        for j in range(weight + 1):
            if j < W[i]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], P[i] + T[i - 1][j - W[i]])

    return get_solution(T, n, weight, P, W), T[n - 1][weight]


def get_solution(T, n, weight, P, W):
    solution = []
    index = weight
    for i in range(n - 1, 0, -1):
        if T[i][index] == T[i - 1][index]:
            continue
        else:
            solution.append((P[i], W[i]))
            index -= W[i]

    solution.reverse()

    return solution


if __name__ == '__main__':
    W = [1, 3, 4, 5] #weigths
    P = [1, 4, 5, 7] #values
    print(knapsack(W, P, 7))
