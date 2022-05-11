# Wyjeżdżacie ze znajomymi na wakajce. Macie dwa samochody i N bagaży o łącznej wadze W. Waga każdego z bagaży jest liczbą naturalną dodatnią. Czy
# jesteście w stanie tak je zapakować, aby w obu samochodach były bagaże o tej samej łącznej wadze

def packing(T):
    N = len(T)
    W = sum(T)
    T.sort()
    if W % 2 != 0:
        return False

    tab = [[False for _ in range((W // 2) + 1)] for _ in range(N)]
    tab[0][T[0]] = True
    tab[0][0] = True

    for i in range(1, N):
        for j in range((W // 2) + 1):
            if T[i] > j:
                tab[i][j] = tab[i - 1][j]
            else:
                tab[i][j] = tab[i - 1][j] or tab[i - 1][j - T[i]]

    return tab[N - 1][W // 2]


if __name__ == '__main__':
    t = [50, 50, 100]
    t1 = [2, 2, 2, 2, 8, 16]
    t2 = [3, 5, 1, 3, 3, 2]
    print(packing(t2))





