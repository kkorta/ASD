def mergesort(T):
    if len(T) > 1:
        mid = len(T) // 2
        left = T[:mid]
        right = T[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                T[k] = left[i]
                i += 1
            else:
                T[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            T[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            T[k] = right[j]
            j += 1
            k += 1

    return T


def create_tab(T):
    for i in range(len(T)):
        T[i] = [T[i], i]

    return T


def chaos_index(T):
    create_tab(T)
    mergesort(T)
    max_dif = 0
    for i in range(len(T)):
        if abs(i - T[i][1]) > max_dif:
            max_dif = abs(i - T[i][1])

    return max_dif
