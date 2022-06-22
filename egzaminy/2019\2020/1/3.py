from math import log


def insert_sort(T):
    for i in range(1, len(T)):
        value = T[i]
        k = i - 1
        while k >= 0 and T[k] > value:
            T[k + 1] = T[k]
            k = k - 1
        T[k + 1] = value
    return T


def fast_sort(tab, a):
    n = len(tab)
    buckets = [[] for _ in range(n + 1)]
    for i in range(n):
        num = log(tab[i], a)
        index = int(a * num)
        buckets[index].append(tab[i])

    for i in buckets:
        insert_sort(i)

    result = [None] * n
    k = 0
    for i in buckets:
        for j in i:
            result[k] = j
            k += 1

    return result

