def binary_search(A, i, j, k, t):
    while j-i > 1:
        m = i + (j-i)//2
        if t[A[m]] >= k:
            j = m
        else:
            i = m
    return j

def lis(t):
    n = len(t)
    a = [0] * (n + 1)
    size = 0
    for i in range(1, n):
        if t[a[size]] < t[i]:
            size += 1
            a[size] = i
        elif t[a[size]] > t[i]:
            index = binary_search(a, -1, size, t[i], t)
            a[index] = i

    return size + 1