def longest_common_subsequence(array_1: list, array_2: list):
    """Наибольшая общая последовательность"""
    f = [[0]*(len(array_2)+1) for i in range(len(array_1)+1)]
    for i in range(1, len(array_1)+1):
        for j in range(1, len(array_2)+1):
            if array_1[i-1] == array_2[j-1]:
                f[i][j] = 1 + f[i-1][j-1]
            else:
                f[i][j] = max(f[i][j-1], f[i-1][j])
    return f[-1][-1]


def test_subsequence(func):
    a = [1, 3, 5, 7]
    b = [3, 3, 6, 7, 4]

    print(f'test OK\nlong common subsequence = {func(a,b)}'
          if func(a,b) == 2 else
          f'test Fail\nlong common subsequence = {func(a,b)}')


test_subsequence(longest_common_subsequence)
