from math import inf

def min_steps(t):
    n = len(t)
    steps = [inf] * n
    steps[0] = 0
    places = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if t[j] + j >= i:
                if steps[j] + 1 < steps[i]:
                    steps[i] = steps[j] + 1
                    places[i] = j

    return steps[n - 1], get_solution(places, n)


def get_solution(places, n):
    index = n - 1
    solution = []
    while places[index] != -1:
        index = places[index]
        solution.append(index)

    solution.reverse()
    return solution


if __name__ == '__main__':
    tab = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
    print(min_steps(tab))