def count_trajectory(n, allowed: list):
    """Функция подсчета возможных траекторий с возможностью запрета точек передвижения"""
    dist = [0, 1, int(allowed[2])] + [0]*(n-2)
    for i in range(3, n+1):
        if allowed[i]:
            dist[i] = dist[i-3]+dist[i-2]+dist[i-1]
    return dist[n]


print(count_trajectory(6, [1, 1, 1, 1, 0, 0, 1]))
