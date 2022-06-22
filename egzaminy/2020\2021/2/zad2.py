from zad2testy import runtests
from math import inf




class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi
        self.sums = 0

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)


def seek_sums(T):
    for i in range(len(T.edges)):
        seek_sums(T.edges[i])
        T.sums += T.edges[i].sums + T.weights[i]

    return T


def seek_result(T, s,):
    for i in range(len(T.edges)):
        curr_min = abs(2 * T.edges[i].sums - s + T.weights[i])
        if index[0] > curr_min:
            index[1] = T.ids[i]
            index[0] = curr_min
            seek_result(T.edges[i], s)

    return index


def balance( T ):
    seek_sums(T)
    global index
    index = [inf, -1]
    seek_result(T, T.sums)
    return index[1]

    
runtests( balance )


