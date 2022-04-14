from math import *


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None


def value(node, index):
    if index == 1:
        return node.key

    height = 2 ** (int(floor(log(index, 2))) - 1)
    new_index = height + (index % height)

    if index < 3 * height:
        return value(node.left, new_index)
    return value(node.right, new_index)


def maxim(T, X):
    max_ = -inf
    for i in X:
        p = T
        max_ = max(max_, value(p, i))

    return max_
