# W porcie na odbiór oczekuje n kontenerów z towarem. Waga każdego kontenera jest znana i
# zapisana w tablicy T (w kilogramach). Dwuczęściowy kontenerowiec, który przypłynął
# odebrać towar jest ogromny - na tylko jednej z jego części zmieściłyby się wszystkie
# oczekujące kontenery. Jednak ze względów technicznych, aby statek nie zatonął, w każdej z
# dwóch jego części musi znajdować się towar o tej samej łącznej wadze. Z tego względu
# władze portowe muszą zaopatrzyć statek w pewną ilość kilogramowych odważników, które
# pozwolą na wyrównanie wagi w obydwu jego częściach. Odważniki te jednak są drogie, więc
# zależy im na tym, aby użyć ich jak najmniej. Twoim zadaniem jako programisty jest napisanie
# programu, który policzy, jaka jest ta najmniejsza możliwa liczba odważników.
# Algorytm należy zaimplementować jako funkcję postaci:
# def kontenerowiec( T ):
# ...
# która przyjmuje tablicę wag kontenerów T i zwraca najmniejszą konieczną liczbę
# odważników, które trzeba umieścić na statku.
# Przykład. Dla danych:
# T = [1, 6, 5, 11]
# Wynikiem jest liczba 1

def kontnerowiec(T):
    weight = sum(T)
    n = len(T)
    tab = [[False for _ in range((weight // 2) + 1)] for _ in range(n)]
    tab[0][T[0]] = True
    tab[0][0] = True

    for i in range(1, n):
        for j in range((weight // 2) + 1):
            if T[i] > j:
                tab[i][j] = tab[i - 1][j]
            else:
                tab[i][j] = tab[i - 1][j] or tab[i - 1][j - T[i]]

    index = weight // 2
    while tab[n - 1][index] is not True:
        index -= 1

    return weight - (2 * index)

import time

TEST_SPEC = [
# N (długość tablicy), m (min. liczba), M (max. liczba), hint (poprawna odpowiedź)
  (0, 0, 0, 1),
  (0, 0, 0, 3),
  (0, 0, 0, 13),
  (5, 20, 100, 91),
  (7, 200, 1000, 881),
  (9, 500, 2500, 1867),
  (13, 1000, 5000, 2606),
  (15, 2000, 10000, 1344),
  (25, 2000, 5000, 0),
  (17, 200, 15000, 14401)
]

MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32

def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed

def runtests( f ):
    total = 0
    zaliczone = 0
    testy = 0
    i = 0
    for el in TEST_SPEC:
        T = []
        for j in range(el[0]):
            T.append(MY_random()%el[1]+el[2])
        if i == 0:
            T = [1, 6, 5, 11]
        if i == 1:
            T = [1, 4]
        if i == 2:
            T = [20, 19, 18, 20, 16]
        start = time.time()
        sol = f(T)
        end = time.time()
        total += (end-start)
        testy += 1
        if sol == el[3]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))
runtests(kontnerowiec)