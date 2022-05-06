# min number of edits to convert word a to b

def no_of_edits(a, b):
    n = len(a)
    m = len(b)

    tab = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, n + 1):
        tab[0][i] = i
    for i in range(1, m + 1):
        tab[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[j - 1] == b[i - 1]:
                tab[i][j] = tab[i - 1][j - 1]
            else:
                tab[i][j] = min(tab[i - 1][j] + 1, tab[i][j - 1] + 1, tab[i - 1][j - 1] + 1)

    return tab[m][n]

if __name__ == '__main__':
    a = "swidry"
    b = "kawiory"
    print(no_of_edits(a, b)) # 1 k + swidry = kswidry, 2 s = a -> kawidry, 3 d = o -> kawiory