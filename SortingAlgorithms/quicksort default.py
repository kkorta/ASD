def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quicksort(T, p, r):
    if len(T) == 1:
        return T
    if p < r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        quicksort(T, q+1, r)