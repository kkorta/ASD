def mergesort(T):
    if len(T) > 1:
        mid = len(T) // 2
        left = T[:mid]
        right = T[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
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



