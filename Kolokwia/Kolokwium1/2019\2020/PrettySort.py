def convert_to_pretty(x):
    count = [0] * 10
    num = x
    while num != 0:
        count[num % 10] += 1
        num //= 10

    single = 0
    many = 0
    for i in range(10):
        if count[i] == 1:
            single += 1
        elif count[i] > 1:
            many += 1

    return x, single, many


def counting_sort(T, index, n):
    C = [0] * 10
    B = [0] * n

    for x in T:
        C[x[index]] += 1

    for i in range(1, 10):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[T[i][index]] - 1] = T[i]
        C[T[i][index]] -= 1


    if index == 1:
        counter = 0
        for i in range(n - 1, -1, -1):
            T[counter] = B[i]
            counter += 1
    else:
        for i in range(n):
            T[i] = B[i][0]


    return T

def pretty_sort(T):
    n = len(T)
    for i in range(n):
        T[i] = convert_to_pretty(T[i])

    counting_sort(T, 1, n)
    counting_sort(T, 2, n)



    return T




T = [123, 455, 2344, 2145]
T2 = [11111, 245, 566, 7889, 1224455, 99883361, 5]
print(pretty_sort(T2))