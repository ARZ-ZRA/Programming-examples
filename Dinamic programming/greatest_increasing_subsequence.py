def gis(a: list):
    f = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        m = 0
        for j in range(i):
            if a[i - 1] > a[j - 1] and f[j] > 0:
                m = f[j]
        f[i] = m + 1
    return f[len(a)]


print(gis([2, 4, 5, 1, 7, 8]))


def longest_increase_sequence(array: list):  # Мой вариант функции выше
    """Нахождение наибольшей возрастающей подпоследовательности"""
    f = [[0] for i in range(len(array) - 1)]
    for i in range(len(array) - 1):
        if array[i] >= array[i - 1]:
            f[i] = f[i - 1] + 1
        else:
            f[i] = 1
    return f[-1]

# print(longest_increase_sequence([2, 4, 5, 6, 7, 8]))
