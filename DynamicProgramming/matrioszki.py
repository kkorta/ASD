def matrioszki(T):
    T.sort(reverse=True)
    n = len(T)
    f = [1] * n
    for i in range(1, n):
        for j in range(i):
            if T[i][1] < T[j][1] and f[i] < f[j] + 1 and T[i][0] != T[j][0]:
                f[i] = f[j] + 1

    return max(f)


if __name__ == '__main__':
    t = [(5, 3), (3, 2), (2, 1), (1, 5), (1, 4)]
    print(matrioszki(t))