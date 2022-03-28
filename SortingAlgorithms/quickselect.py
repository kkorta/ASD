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


def select(T, p, r, k):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if q == k:
        return T[q]
    elif k < q:
        return select(T, p, q-1, k)
    else:
        return select(T, q+1, r, k)


if __name__ == '__main__':
    T = [randint(1, 25) for _ in range(10)]
    print(T)
    select(T, 0, 9, 8)
    select(T, 0, 9, 1)
    print(T)

