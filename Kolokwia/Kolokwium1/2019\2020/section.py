def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def select(T, p, r, k):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if q == k:
        return T[q]
    elif k < q:
        return select(T, p, q - 1, k)
    else:
        return select(T, q + 1, r, k)


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

def section(T, p, q):
    length = q - p + 1
    order = [0] * length
    n = len(T)
    select(T, 0, n - 1, q)
    select(T, 0, n - 1, p)
    quickersort(T, p, q + 1)
    print(T)
    index = length - 1
    for i in range(p, q + 1):
        order[index] = T[i]
        index -= 1

    return order

