from math import inf
from queue import PriorityQueue


def switch(x, y, direction):
    if direction == 0:
        return x + 1, y
    if direction == 1:
        return x, y + 1
    if direction == 2:
        return x - 1, y
    if direction == 3:
        return x, y - 1


def robot(L, A, B):
    n = len(L)
    m = len(L[0])
    graph = [[[[inf, inf, inf] for _ in range(4)] for _ in range(m)] for _ in range(n)]
    seconds = [60, 40, 30]
    pq = PriorityQueue()
    pq.put((0, A[0], A[1], 0, 0))
    while not pq.empty():
        time, x, y, direction, num = pq.get()
        if (x, y) == B:
            return time
        if graph[y][x][direction][num] == inf and L[y][x] != 'X':
            graph[y][x][direction][num] = time
            pq.put((time + 45, x, y, (direction + 1) % 4, 0))
            pq.put((time + 45, x, y, (direction + 3) % 4, 0))

            a, b = switch(x, y, direction)
            if num == 2:
                pq.put((time + seconds[num], a, b, direction, 2))
            else:
                pq.put((time + seconds[num], a, b, direction, num + 1))

