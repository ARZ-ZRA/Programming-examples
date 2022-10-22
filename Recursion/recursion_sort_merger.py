def recursion_sort_merger(array: list):
    ''' Сортировка массива методом слияния '''
    if len(array) <= 1:
        return
    half = len(array) // 2
    array_sort = []
    array_l = [array[i] for i in range(half)]
    array_r = [array[i] for i in range(half, len(array))]
    recursion_sort_merger(array_l)
    recursion_sort_merger(array_r)
    sort_ = sort(array_l, array_r)
    for i in range(len(array)):
        array[i] = sort_[i]


def sort(array_l: list, array_r: list):
    array_gen = [0]*(len(array_l)+len(array_r))
    i, k, n = 0, 0, 0
    while i < len(array_l) and k < len(array_r):
        if array_l[i] <= array_r[k]:
            array_gen[n] = array_l[i]
            i += 1
        else:
            array_gen[n] = array_r[k]
            k += 1
        n += 1
    while i < len(array_l):
        array_gen[n] = array_l[i]
        i += 1
        n += 1
    while k < len(array_r):
        array_gen[n]  = array_r[k]
        k += 1
        n += 1
    return array_gen


def test_merger(func):
    array = [4, 7, 8, 4, 3, 0, 65, 4, 3]
    array_copy = array.copy()
    array_sort = sorted(array_copy)
    func(array)
    print(f'test OK\n{array_sort}\n{array}' if array_sort == array else f'test Fail {array_sort}\n{array}')

    from random import randint
    array1 = list()
    for i in range(50):
        array1.append(randint(25, 500))
    array1_copy = array1.copy()
    array1_sort = sorted(array1_copy)
    func(array1)
    print(f'test OK\n{array1_sort}\n{array1}' if array1_sort == array1 else f'test Fail {array1_sort}\n{array1}')




test_merger(recursion_sort_merger)