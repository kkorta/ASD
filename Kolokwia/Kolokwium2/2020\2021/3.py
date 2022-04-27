
from pprint import pprint
from queue import PriorityQueue

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
    visited = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        if T[0][i] != 0 and visited[0][i] == -1:
            T[0][i] = count(T, visited, 0, i, 0)

        elif T[0][i] != 0 and visited[0][i] == 1:
            T[0][i] = 0

    return T


def plan(T):

    solution = []
    n = len(T[0])
    T = collect_oil(T, n)
    fuel = T[0][0]
    solution.append(0)
    q = PriorityQueue()
    i = 1
    while fuel < n and i < n:
        if i <= fuel and T[i] != 0:
            q.put((-T[0][i], i))

        if fuel < i:
            val, pos = q.get()
            fuel -= val
            if T[0][i] != 0:
                q.put((-T[0][i], i))
            solution.append(pos)

        i += 1

    return sorted(solution)

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
