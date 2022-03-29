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



def sumBetween(T, s, e):
     n = len(T)
     quick_select(T, 0, n - 1, s)
     quick_select(T, 0, n - 1, e)
     print(T)
     counter = 0
     for i in range(s, e + 1):
         counter += T[i]

     return counter






