def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_select(T, p, r, x):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if x == q:
        return T[x]
    elif x > q:
        return quick_select(T, q + 1, r, x)
    else:
        return quick_select(T, p, q - 1, x)



def linear(T, n):
    tab = [0] * (n * n)
    index = 0
    for i in range(n):
        for j in range(n):
            tab[index] = T[i][j]
            index += 1

    return tab


def Median(T):
    n = len(T)
    tab = linear(T, n)
    interval = ((n * n) - n )// 2
    quick_select(tab, 0, n * n - 1, interval)
    quick_select(tab, 0, n * n - 1, n * n - interval)

    index = interval
    for i in range(n):
        T[i][i] = tab[index]
        index += 1

    index = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            T[j][i] = tab[index]
            index += 1


    index = n * n - interval - 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            T[i][j] = tab[index]
            index += 1


    return T
