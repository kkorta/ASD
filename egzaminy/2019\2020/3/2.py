def tower(T):
    n = len(T)
    f = [1] * n

    for i in range(1, n):
        for j in range(i):
            if T[i][1] <= T[j][1] and T[j][0] <= T[i][0] and f[i] < f[j] + 1:
                f[i] = f[j] + 1

    return max(f)


TESTS = [

    ([(1, 4), (0, 6), (1, 5), (2, 4), (2, 4), (2, 3)], 5),
    ([(1, 4), (0, 6), (1, 5), (2, 4), (2, 4), (2, 3), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2)], 6),
    ([(1, 6), (2, 7), (3, 4), (2, 7), (2, 7)], 3),
    ([(1, 4), (0, 5), (1, 5), (2, 6), (2, 4)], 3),

]


def runtests(f):
    OK = True
    for (dane, res) in TESTS:
        y = f(dane)

        print("----------------------")
        print("A =", dane)
        print("oczekiwany wynik =", res)
        print("otrzymany wynik  =", y)

        if res != y:
            print("Blad!")
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")

runtests(tower)