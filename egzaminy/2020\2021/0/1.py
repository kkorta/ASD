def counting_sort(t):
    n = len(t)
    c = [0] * 26
    b = [0] * n
    for i in range(n):
        c[ord(t[i][0]) - ord('a')] += 1

    for i in range(1, 26):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        c[ord(t[i][0]) - ord('a')] -= 1
        b[c[ord(t[i][0]) - ord('a')]] = t[i]

    for i in range(n):
        t[i] = b[i]

    return t


def tanagram(x, y, t):
    n = len(x)
    n2 = len(y)
    if n != n2:
        return False

    t1 = [[0, 0] for _ in range(n)]
    t2 = [[0, 0] for _ in range(n)]
    for i in range(n):
        t1[i][0], t1[i][1] = x[i], i
        t2[i][0], t2[i][1] = y[i], i

    counting_sort(t1)
    counting_sort(t2)
    for i in range(n):
        if abs(t1[i][1] - t2[i][1]) > t:
            return False

    return True


x = 'kotomysz'
y = 'tokmysoz'
print(tanagram(x, y, 3))

