def graph_traversal_in_depth(graph: list = [(0, 1), (0, 2), (0, 3), (3, 5), (5, 4), (5, 6), (5, 7), (1, 4)],  \
                    top: list = [0, 1, 2, 3, 4, 5, 6, 7], \
                    node: int = 0):
    """ Поиск в глубину по графу с использованием стэка
    >>> graph_traversal_in_depth()
    [True, True, True, True, True, True, True, True]
    """

    stack = []
    visited = [False for i in top]
    stack.append(node)
    while bool(stack):
        visited[stack.pop()] = True
        for i, j in graph:
            if not visited[i]:
                if i not in stack and i == i-1:
                    stack.append(i)
            elif visited[i] and not visited[j]:
                if j not in stack:
                    stack.append(j)
    return visited


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)






