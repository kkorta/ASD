from zad3testy import runtests

def lamps(n, L):
    tab = [0] * n
    curr = 0
    result = 0
    for i in L:
        for j in range(i[0], i[1] + 1):
            if tab[j] == 0:
                tab[j] = 1
            elif tab[j] == 1:
                tab[j] = 2
                curr += 1
            else:
                tab[j] = 0
                curr -= 1

        if curr > result:
            result = curr

    return result


runtests(lamps)