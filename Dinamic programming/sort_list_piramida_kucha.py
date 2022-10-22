"""Сортировка списка с использованием метода Пирамиды (Куча)"""

def count_top_piramida(list: list):
    """
    Функция нахождения количества вершин пирамиды
    >>> count_top_piramida(list(range(1, 8)))
    3
    >>> count_top_piramida(list(range(1, 9)))
    4
    """
    if len(list) > 0:
        i = 1
        top = 1
        while i < len(list):
            i = 2**top
            if i <= len(list):
                top += 1
            else:
                break
    return top


def sort_descending_piramida(list: list):
    """
    Функция сортировки подготовленного списка по убыванию,длинна которого
    кратна 2^N
    >>> sort_descending_piramida(list(range(1,8)))
    [7, 6, 5, 4, 3, 2, 1]
    >>> sort_descending_piramida(list(range(1,16)))
    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    if len(list) > 0:
        k = 1
        top = count_top_piramida(list)
        global flag
        flag = True
        q = 0
        while flag:
            while k < top:
                for i, j in zip(range(2**top//2-1), range(2**top//2-1)):
                    """ Проверка условия наибольшего элемента слева """
                    if list[(2**k-1)+j] > list[(2**(k-1)-1)+i]:
                        list[(2**k - 1) + j], list[(2**(k-1)-1)+i] = \
                            list[(2**(k-1)-1)+i], list[(2**k - 1) + j]
                    """ Проверка условия наибольшего элемента справа """
                    if list[(2**k-1)+j+1] > list[(2**(k-1)-1)+i]:
                        list[(2**k - 1) + j + 1], list[(2**(k-1)-1)+i] = \
                            list[(2**(k-1)-1)+i], list[(2**k - 1) + j + 1]
                    """ Сортировка элементов ("листьев") на последнем уровне """
                    if k == top-1 and list[(2**k-1)+j] < list[(2**k-1)+j+1]:
                        list[(2**k-1)+j], list[(2**k-1)+j+1] = \
                            list[(2**k-1)+j+1], list[(2**k-1)+j]
                k += 1
            """ Проверка порядка данных в списке после первого прохода.
                Если остаются неупорядоченные элементы => функция проходит
                еще круг перестановок """
            for i in range(1, len(list)):
                if list[i] <= list[i - 1]:
                    k = 1
                    if i == len(list)-1:
                        flag = False
                    continue
                else:
                    k = 1
                    break
    return list


def sort_list(list: list):
    """ Функция сортировки, которая приводит входящий список
        данных в список, длинной кратной 2^N .
        возвращает отсортированный список
        >>> sort_list(list(range(1, 9)))
        [1, 2, 3, 4, 5, 6, 7, 8]
        [8, 7, 6, 5, 4, 3, 2, 1]
        >>> sort_list(list(range(34)))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
        [33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        """
    print(list)
    n = count_top_piramida(list)
    k = 0
    if len(list) == 2**n-1:
        sort_descending_piramida(list)
        print(list)
    else:
        for i in range(2**(n-1)-1, len(list)):
            k += 1
        additional = [0]*((2**n-1)-(2**(n-1)-1)-k)
        list = list + additional
        [0] * ((2 ** n - 1) - (2 ** (n - 1) - 1) - k)
        sort_descending_piramida(list)
        for i in range(len(additional)):
            list.pop()
    return list


if __name__ == '__main__':
    import doctest
    doctest.testmod()