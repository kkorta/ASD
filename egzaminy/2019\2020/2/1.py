from math import inf
from queue import PriorityQueue
# dynamicznie
def zbigniew(A):
    n = len(A)
    sum_ = 0
    if n == 0:
        return 0

    elif A[0] >= n - 1:
        return 1

    for i in range(n):
        sum_ += A[i]

    tab = [[inf for _ in range(sum_ + 1)] for _ in range(n)]
    tab[0][A[0]] = 1

    for i in range(1, n):
        for j in range(sum_ + 1):
            if j + 1 <= sum_:
                if tab[i - 1][j + 1] != inf:
                    tab[i][j] = min(tab[i][j], tab[i - 1][j + 1])
                    tab[i][j + A[i]] = min(tab[i][j] + 1, tab[i][j + A[i]])


    return min(tab[n - 1])
#zachlannie
def zbigniew2(A):
    n = len(A)
    energy = A[0]
    q = PriorityQueue()
    i = 1
    counter = 1
    while energy < n and i < n:
        if i <= energy and A[i] != 0:
            q.put((-A[i], i))

        if energy < i:
            val, pos = q.get()
            energy -= val
            if A[i] != 0:
                q.put((-A[i], i))
            counter += 1
        i += 1

    return counter
A1 = [2, 2, 1, 0, 0, 0]
R1 = 3

A2 = [4, 5, 2, 4, 1, 2, 1, 0]
R2 = 2

A3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
R3 = 4

A4 = [4, 2, 2, 2, 1, 2, 1, 1, 0]
R4 = 3

A5 = [4, 3, 0, 1, 2, 0, 1, 0]
R5 = 2

TESTS = [(A1, R1), (A2, R2), (A3, R3), (A4, R4), (A5, R5)]


def runtests(f):
    OK = True
    for (A, R) in TESTS:
        res = f(A)
        print("----------------------")
        print("A =", A)
        print("oczekiwany wynik =", R)
        print("otrzymany wynik  =", res)

        if res != R:
            print("Blad!")
            OK = False
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")


runtests(zbigniew2)