def DFS(graph, root):
    visited = [False] * len(graph)
    result = []
    dfs_visit(root, graph, visited, result)
    print(visited)
    return result


def dfs_visit(u, graph, visited, result):
    visited[u] = True
    result.append(u)
    for i in range(len(graph)):
        if visited[i] is False and graph[u][i] == 1:
            dfs_visit(i, graph, visited, result)


if __name__ == '__main__':
    g = [[0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]]
    print(DFS(g, 5))
