class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.length = 0


def heavy_path(T):
    result = 0

    def recursion(T):
        nonlocal result
        for i in T.child:
            u, w = i[0], i[1]
            u.length = T.length + w
            if u.length > result:
                result = u.length

            recursion(u)

    recursion(T)

    return result


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.child = [(B, 100), (C, -500)]
B.child = [(D, 100), (E, 101)]
C.child = [(F, 1000)]

print(heavy_path(A))