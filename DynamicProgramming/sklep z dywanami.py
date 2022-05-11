# Pewien przedsiębiorca potrzebuje zamówić do swojej firmy dywany o łącznym polu
# powierzchni wynoszącym N metrów kwadratowych. Nie martwi się on jakich będą one
# wymiarów, ponieważ może je w dowolny sposób przycinać i łączyć. Aczkolwiek sklep, w
# którym chce je kupić, sprzedaje tylko kwadratowe dywany o boku długości wyrażoną liczbą
# naturalną określającą długość w metrach. Koszt zapakowania każdego dywanu jest stały
# niezależnie od jego wielkości. Ze względów podatkowych przedsiębiorca potrzebuje
# zminimalizować łączny koszt zapakowania dywanów, które zakupi, jednocześnie dbając o
# środowisko nie może dopuścić, żeby jakikolwiek fragment dywanu się zmarnował. Twoim
# zadaniem jako jego pracownika jest stworzenie listy wymiarów dywanów (wyrażonych jako
# długość ich boku w metrach), które przedsiębiorca musi zakupić.
# Algorytm należy zaimplementować jako funkcję postaci:
# def dywany( N ):
# ...
# która przyjmuje wymagane pole powierzchni dywanów N w metrach kwadratowych, a zwraca
# tablicę długości boków dywanów, które trzeba kupić.
# Przykład. Dla danych:
# N = 6
# Wynikiem jest np. tablica [1, 1, 2]

def dywany(N):
    tab = [[0 for _ in range(N + 1)] for _ in range(N)]

    for i in range(N + 1):
        tab[0][i] = i

    for i in range(1, N):
        for j in range(N + 1):
            if j < (i + 1) * (i + 1):
                tab[i][j] = tab[i - 1][j]
            else:
                tab[i][j] = min(tab[i - 1][j], tab[i][j - ((i + 1) * (i + 1))] + 1)

    solution = []
    index = N
    i = N - 1
    while i > 0 and tab[i][index] != 0:

        if tab[i][index] == tab[i - 1][index]:
            i -= 1
        elif tab[i][index] - 1 == tab[i - 1][index - ((i + 1) * (i + 1))]:
            solution.append(i + 1)
            index -= ((i + 1) * (i + 1))
            i -= 1
        elif tab[i][index] - 1 == tab[i][index - ((i + 1) * (i + 1))]:
            solution.append(i + 1)
            index -= ((i + 1) * (i + 1))

    while tab[i][index] != 0:
        solution.append(i + 1)
        index -= 1
    return solution




import time
import sys

sys.setrecursionlimit(2500)

TEST_SPEC = [
# M (liczba), hint (poprawna odpowiedź)
  (6, 3),
  (100, 1),
  (145, 2),
  (248, 3),
  (542, 3),
  (319, 4),
  (786, 3),
  (791, 4),
  (1372, 4),
  (2168, 3),
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
        start = time.time()
        sol = f(el[0])
        end = time.time()
        total += (end-start)
        testy += 1
        suma = 0
        for ell in sol:
            suma += ell*ell
        if suma == el[0] and len(sol) == el[1]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[1])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[1])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

runtests(dywany)