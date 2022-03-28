import random
def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


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

def check(T):
    n = len(T)
    quickersort(T, 0, n - 1)

    for i in range(n):
        if i + 1 != n and i != 0:
            start = 0
            end = n - 1
        elif i + 1 == n:
            start = 0
            end = i - 1
        else:
            start = 1
            end = n - 1

        while True:
            if T[i] == T[start] + T[end]:
                break
            elif start >= end:

                return False

            elif T[i] > T[start] + T[end]:
                start += 1

            elif T[i] < T[start] + T[end]:
                end -= 1

    return True

arr = [8, 7, 5, 4, 4, 3, 2, 2, 1, 0, -2, -3, -3, -5]
print(check(arr))




