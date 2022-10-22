def recursion_hoar_sort(array):
    """ Сортировка элементов массива с помощью метода Хора (быстрая сортировка)"""
    if len(array) <= 1:
        return
    half = len(array)//2
    barier_element = array[half]
    left_list_array = []
    middle_list_array = []
    right_list_array = []
    for i in array:
        if i < barier_element:
            left_list_array.append(i)
        elif i == barier_element:
            middle_list_array.append(i)
        else:
            right_list_array.append(i)
    recursion_hoar_sort(left_list_array)
    recursion_hoar_sort(right_list_array)
    k = 0
    for i in left_list_array + middle_list_array + right_list_array:
        array[k] = i
        k += 1


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


test_merger(recursion_hoar_sort)