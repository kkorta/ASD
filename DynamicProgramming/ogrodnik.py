# W sadzie pewnego oszczędnego ogrodnika rosły drzewa owocowe. Jednak ze względu na
# brak wystarczającej ilości funduszy, nie ma on możliwości podlania wszystkich z nich. Musi
# wybrać, które drzewa podlać, aby ze sprzedaży owoców z nich zebranych osiągnąć jak
# największy przychód. (Aby podlać dane drzewo musimy podlać cały jego korzeń, tj.
# wszystkie jego fragmenty posiadające przynajmniej jeden wspólny bok). Dana jest tablica
# dwuwymiarowa T o wymiarach NxM która zawiera informacje o tym, czy na danej
# "współrzędnej" znajduje się korzeń jakiegoś drzewa i jeżeli tak, to ile litrów wody wymaga,
# aby został poprawnie podlany. Pierwsza współrzędna tablicy T określa głębokość, a druga
# lokalizację. Ze względów logistycznych ogrodnik posiada księgę, w której zapisane są
# lokalizacje wszystkich drzew w sadzie. Wyrażona jest poprzez tablicę liczb naturalnych D.
# Przykładowo, jeżeli D[i] = x, oznacza to, że w punkcie T[0][x] będzie znajdował się fragment
# korzenia drzewa i-tego. Można założyć, że na głębokości "zerowej" każde drzewo posiada
# tylko jeden fragment korzenia, oraz, że żadne dwa drzewa nie mają wspólnego korzenia.
# Księgowa ogrodnika przygotowała także zbiór (wyrażony tablicą liczb naturalnych Z)
# potencjalnych przychodów, które może osiągnąć ze zbiórki owoców (Tak, że dla drzewa w
# lokalizacji D[i], potencjalny przychód wynosi Z[i]). Proszę napisać algorytm, który zwróci
# maksymalny przychód, który ogrodnik może osiągnąć ze zbiorów, zakładając, że posiada on
# tylko l litrów wody, aby podlać swój ogród.
# Algorytm należy zaimplementować jako funkcję postaci:
# def ogrodnik( T, D, Z, l ):
# ...
# która przyjmuje tablicę dwuwymiarową współrzędnych T, tablicę lokalizacji drzew D, tablicę
# potencjalnych zysków Z oraz limit litrów wody l.
# Przykład. Dla danych:
# D = [4, 9, 12, 16]
# Z = [13, 11, 15, 4]
# l = 32

def count(T, visited, row, col, size):
    if row < 0 or row >= len(T) or col < 0 or col >= len(T[0]) or T[row][col] == 0 or visited[row][col] == 1:
        return size
    else:
        size += T[row][col]
        visited[row][col] = 1
        actual_size = size
        actual_size = count(T, visited, row - 1, col, actual_size)
        actual_size = count(T, visited, row + 1, col, actual_size)
        actual_size = count(T, visited, row, col - 1, actual_size)
        actual_size = count(T, visited, row, col + 1, actual_size)
        return actual_size


def ogrodnik(T, D, Z, l):
    n = len(T)
    m = len(T[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]

    for i in D:
        T[0][i] = count(T, visited, 0, i, 0)

    x = len(Z)
    tab = [[0 for _ in range(l + 1)] for _ in range(x)]


    for i in range(T[0][D[0]], l + 1):
        tab[0][i] = Z[0]

    for i in range(1, x):
        for j in range(l + 1):
            if T[0][D[i]] > j:
                tab[i][j] = tab[i - 1][j]
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i - 1][j - T[0][D[i]]] + Z[i])
    return tab[x - 1][l]


import time
from collections import deque

TEST_SPEC = [
    # D (szerokosc), N (ilosc), H (wysokosc), M (max. woda), W (max. wartosc), LIMIT WODY, WYNIK
    (5, 4, 4, 50, 15, 32, 28),
    (5, 15, 5, 50, 50, 154, 347),
    (5, 25, 5, 50, 50, 264, 535),
    (10, 25, 5, 50, 50, 205, 500),
    (25, 50, 20, 70, 50, 939, 1092),
    (50, 50, 50, 100, 50, 1169, 1145),
    (100, 100, 50, 120, 50, 2619, 2152),
    (150, 250, 50, 50, 50, 3075, 5194),
    (100, 400, 50, 10, 50, 1213, 8284),
    (150, 650, 50, 5, 50, 894, 13214),
]

MY_seed = 42
MY_a = 134775813
MY_c = 1
MY_modulus = 2 ** 32


def MY_random():
    global MY_seed, MY_a, MY_c, MY_modulus
    MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
    return MY_seed


total = 0


def bfs(T, V, y, m, D, N, H, M, W):
    global total
    Q = deque()
    V[0][y] = MY_random() % (m // 10 + 1) + 1
    total += V[0][y]

    Q.append((1, y))
    col = 0

    while Q and col < m:
        u = Q.popleft()

        if V[u[0]][u[1]] != 0:
            continue

        r = MY_random() % (m // 10 + 1) + 1
        V[u[0]][u[1]] = r
        col += r
        total += r

        if u[0] - 1 >= 1 and T[u[0] - 1][u[1]] != 0:
            Q.append((u[0] - 1, u[1]))
        if u[0] + 1 < H and T[u[0] + 1][u[1]] != 0:
            Q.append((u[0] + 1, u[1]))
        if u[1] - 1 >= 0 and T[u[0]][u[1] - 1] != 0:
            Q.append((u[0], u[1] - 1))
        if u[1] + 1 < N * D + 1 and T[u[0]][u[1] + 1] != 0:
            Q.append((u[0], u[1] + 1))


def runtests(f, all_tests=True):
    global total
    global TEST_SPEC
    zaliczone = 0
    testy = 0
    ii = 0
    totaltime = 0
    if all_tests == False:
        TEST_SPEC = [TEST_SPEC[0], TEST_SPEC[1], TEST_SPEC[2]]
    for el in TEST_SPEC:
        D = el[0]
        N = el[1]
        H = el[2]
        M = el[3]
        W = el[4]

        total = 0
        DD = []
        ZZ = []

        T = [[MY_random() % (4) for _ in range(N * D + 1)] for _ in range(H)]
        V = [[0 for _ in range(N * D + 1)] for _ in range(H)]

        for i in range(N * D + 1):
            T[0][i] = 0
            T[1][i] = 0

        for i in range(N):
            for e in range(H):
                T[e][i * D] = 0

        for i in range(N):
            r = MY_random() % (D - 1) + 1
            T[0][r + i * D] = 1
            T[1][r + i * D] = 1
            DD.append(r + i * D)
            ZZ.append(MY_random() % (W) + 1)
            m = MY_random() % (M + 1) + M // 10
            bfs(T, V, r + i * D, m, D, N, H, M, W)

        start = time.time()
        sol = f(V, DD, ZZ, total // 2)

        end = time.time()
        totaltime += (end - start)
        testy += 1
        if sol == el[6]:
            print("TEST #", ii, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[6])
            print("Czas trwania: %.2f sek.\n" % float(end - start))
            zaliczone += 1
        else:
            print("TEST #", ii, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[6])
            print("Czas trwania: %.2f sek.\n" % float(end - start))

        ii += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." % float(totaltime))


runtests(ogrodnik)