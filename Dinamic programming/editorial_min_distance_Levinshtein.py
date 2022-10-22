def editorial_min_distance(string_1: str, string_2: str):
    """Редакционное расстояние между строками (Левинштайна)"""
    f = [[(i+j) if i*j == 0 else 0 for j in range(len(string_2)+1)]
         for i in range(len(string_1)+1)]
    for i in range(1, len(string_1)+1):
        for j in range(1, len(string_2)+1):
            if string_1[i-1] == string_2[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
    return f[-1][-1]


print(editorial_min_distance('колокол', 'молоко'))
