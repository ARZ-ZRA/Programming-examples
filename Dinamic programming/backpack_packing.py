def backpack_packing(array_n: list, array_m: list, dedline):
    f = [[0] * (len(array_n) + 1) for i in range(dedline + 1)]
    # n = 0
    # for i in f:
    #
    #     print(f'{n}  {i}')
    #     n += 1

    for i in range(1, len(array_n) + 1):
        print(i)
        for k in range(1, dedline + 1):

            if array_m[i-1] >= k:
                f[i][k] = max(f[i-1][k], (array_n[i-1] + f[i-1][k-array_n[i]]))
                print(f'q {f}')
            else:
                f[i][k] = f[i][k-1]
                print(f'h {f}')
    return f[-1][-1]


print(backpack_packing([3, 5, 4, 2], [5, 10, 6, 5], 14))