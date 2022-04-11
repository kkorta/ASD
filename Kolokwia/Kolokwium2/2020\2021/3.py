from math import inf


def count(T, visited, row, col, size):
    if row < 0 or row >= len(T) or col < 0 or col >= len(T) or T[row][col] == 0 or visited[row][col] == 1:
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


def collect_oil(T, n):
    m = len(T)
    total_oil = 0
    visited = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        if T[0][i] != 0 and visited[0][i] == -1:
            T[0][i] = count(T, visited, 0, i, 0)
            total_oil += T[0][i]

        elif T[0][i] != 0 and visited[0][i] == 1:
            T[0][i] = 0

    return T, total_oil


def plan(T):
    n = len(T[0])
    T, x = collect_oil(T, n)
    tab = [[inf for _ in range(x + 1)] for _ in range(n)]
    if x == 1:
        return [0]

    tab[0][T[0][0]] = 1

    for i in range(1, n):
        for j in range(x + 1):
            if j + 1 < x + 1:
                tab[i][j] = min(tab[i][j], tab[i - 1][j + 1])
                if j + T[0][i] < x + 1 and tab[i - 1][j + 1] != inf:
                    tab[i][j + T[0][i]] = min(tab[i][j + T[0][i]], tab[i][j] + 1)

    index = 0
    minim = inf
    for i in range(x + 1):
        if tab[n - 1][i] <= minim and tab[n - 1][i] != inf:
            minim = tab[n - 1][i]
            index = i


    return get_solution(T, tab, index, n, x + 1)

def get_solution(T, tab, index, n, s):
    height = n - 1
    solution = []
    while tab[height][index] != inf and height > 0 and index >= 0:
        if index + 1 < s:
            if tab[height][index] == tab[height - 1][index + 1]:
                height -= 1
                index += 1

        if T[0][height] != 0 and index - T[0][height] >= 0:
            if tab[height][index] == tab[height][index - T[0][height]] + 1:
                solution.append(height)
                index -= T[0][height]


    solution.append(0)
    solution.reverse()
    return solution

from pprint import pprint

T0 = [
    [1, 0],
    [0, 0],
]

T1 = [
    [3, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T2 = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

T3 = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

r0_T4 = [6, 0, 2, 0, 3, 0, 1, 0, 1, 0, 0, 1]
T4 = [
         r0_T4
     ] + (
             [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (len(r0_T4) - 1)
     )

T5 = [
    [1, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

T6 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T7 = [
    [5, 0, 1, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
]

TESTS = [
    (T0, [0]),
    (T1, [0, 3]),
    (T2, [0, 4]),
    (T3, [0, 2]),
    (T4, [0, 2, 4]),
    (T5, [0, 2, 7]),
    (T6, [0]),
    (T7, [0, 5]),
]


def runtests(f):
    OK = True
    for no, (T, expected) in enumerate(TESTS):
        print(f"---------------------- #{no}")
        print("T: ")
        pprint(T)
        print(f"oczekiwany wynik: {expected}")
        assert all(len(T[i]) == len(T) for i in range(len(T))), f"len(T): {len(T)}, len(T[0]): {len(T[0])}"
        actual = f(T)
        print(f"uzyskany wynik  : {actual}")
        if actual != expected:
            print("PROBLEM!!!!!!")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")
# T3 = [
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
#     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
# T = [2, 0, 2, 1, 1, 1]
# print(plan(T3))

runtests(plan)