from zad7testy import runtests


def hamilton_path(g, n, v, direction, path):
    path.append(v)
    if len(path) == n and 0 in g[path[n - 1]][direction]:
        return path

    for e in g[v][direction]:
        if e in path:
            continue

        if v in g[e][0]:
            direction = 1
        else:
            direction = 0
        res_path = [i for i in path]
        tmp = hamilton_path(g, n, e, direction, res_path)
        if tmp is not None:
            return tmp


def droga(G):
    n = len(G)
    tab = hamilton_path(G, n, 0, 0, [])
    return tab


runtests(droga)
