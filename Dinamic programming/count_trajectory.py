def count_trajectory(n):
    """Функция подсчета возможных траекторий"""
    distance = [0, 1]+[0]*(n-1)

    for i in range(2, n+1):
        distance[i] = distance[i-1]+distance[i-2]
    return distance[n]


print(count_trajectory(6))
