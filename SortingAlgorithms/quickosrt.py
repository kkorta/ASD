from random import randint


def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quickersort(T, p, r):
    while p < r:
        q = partition(T, p, r)

        if (q - p) < (r - q):
            quickersort(T, p, q-1)
            p = q + 1
        else:
            quickersort(T, q+1, r)
            r = q - 1

    return T




n = 10
arr = [20, 8, 7, 5, 4, 4, 3, 2, 2, 1, 0, -2, -3, -3, -5]
T = quickersort(arr, 0, 14)
print(T)
