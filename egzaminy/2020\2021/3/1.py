# O(N^2) , można zrobić nlogn używając LIS nlogn zamiast n^@

def mr(X):
    n = len(X)
    t_back = [1] * n
    p_back = [-1] * n
    t_forward = [1] * n
    p_forward = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if X[i] < X[j] and t_back[i] < t_back[j] + 1:
                t_back[i] = t_back[j] + 1
                p_back[i] = j

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if X[i] < X[j] and t_forward[i] < t_forward[j] + 1:
                t_forward[i] = t_forward[j] + 1
                p_forward[i] = j

    max_ = 0
    index = 0

    for i in range(n):
        if t_back[i] + t_forward[i] - 1 > max_:
            max_ = t_back[i] + t_forward[i] - 1
            index = i

    solution = [0] * max_

    if index == 0 or index == n - 1:
        return X
    else:
        index1 = t_back[index] - 1
        solution[index1] = X[index]
        i, j = p_back[index], p_forward[index]
        i1, i2 = index1 - 1, index1 + 1

        while p_back[i] != -1:
            solution[i1] = X[i]
            i1 -= 1
            i = p_back[i]

        while p_forward[j] != -1:
            solution[i2] = X[j]
            i2 += 1
            j = p_forward[j]

        solution[0] = X[i]
        solution[max_ - 1] = X[j]
        return solution
