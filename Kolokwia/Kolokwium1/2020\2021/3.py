from math import inf, ceil, floor


def selection_sort(T):
    n = len(T)
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if T[index] > T[j]:
               index = j

        T[i], T[index] = T[index], T[i]

    return T


def SortTab(T, P):

    max_ = -inf
    min_ = inf
    n = len(T)
    for i in P:
        if i[0] < min_:
            min_ = i[0]
        if i[1] > max_:
            max_ = i[1]

    buckets_no = ceil(max_ - min_ + 1)
    buckets = [[] for _ in range(buckets_no)]

    for i in range(n):
        index = floor(T[i] - min_)
        buckets[index].append(T[i])

    counter = 0
    for i in buckets:
        selection_sort(i)
        for j in i:
            T[counter] = j
            counter += 1


    return T

if __name__ == '__main__':
    T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
    P = [(1, 5, 0.75), (4, 8, 0.25)]
    print(SortTab(T, P))

