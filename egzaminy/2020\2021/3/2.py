from zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.c = 0
        self.w = ''


def create_tree(L):
    x = Node()

    for i in L:
        p = x
        for j in range(len(i)):
            if i[j] == '0' and p.left is None:
                p.left = Node()
                p.left.parent = p
                p.left.c += 1
                p.left.w = p.w + '0'
                p = p.left
            elif i[j] == '0' and p.left is not None:
                p.left.c += 1
                p.left.w = p.w + '0'
                p = p.left
            elif i[j] == '1' and p.right is None:
                p.right = Node()
                p.right.parent = p
                p.right.c += 1
                p.right.w = p.w + '1'
                p = p.right
            else:
                p.right.c += 1
                p.right.w = p.w + '1'
                p = p.right
    x.c = 2
    return x


def recursion(x, word):
    if x.left is not None and x.left.c >= 2:
        recursion(x.left, word)
    if x.right is not None and x.right.c >= 2:
        recursion(x.right, word)

    if (x.right is None and x.left is None) or (x.right is not None and x.right.c < 2 and x.left is None) or (x.left is not None and x.left.c < 2 and x.right is None) or \
            (x.left is not None and x.right is not None and x.left.c < 2 and x.right.c < 2):
        word.append(x.w)

    return word



def double_prefix( L ):
    x = create_tree(L)
    return recursion(x, [])

runtests( double_prefix )

