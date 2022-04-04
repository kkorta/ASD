def lis(num):
    n = len(num)
    t = [1] * n
    p = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if num[i] > num[j] and t[i] < t[j] + 1:
                t[i] = t[j] + 1
                p[i] = j

    return max(t), get_solution(t, p, n)



def get_solution(t, p, n):
    solution = []
    index = 0
    maxy = 0
    for i in range(n):
        if t[i] > maxy:
            maxy = t[i]
            index = i

    while p[index] != -1:
        solution.append(index)
        index = p[index]

    solution.append(index)
    solution.reverse()
    return solution


if __name__ == '__main__':
    t = [4, 0, -1, 7]
    t2 = [3, 4, -1, 0, 6, 2, 3]
    print(lis(t2))

