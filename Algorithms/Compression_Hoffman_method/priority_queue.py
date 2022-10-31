from count_symbols import count_symbol


def find_top(list: list):
    """
    Функция подсчёта уровней (вершин) пирамиды (кучи)
    """
    if len(list) > 0:
        i, top = 1, 1
        while True:
            i = 2 ** top
            if i <= len(list):
                top += 1
            else:
                break
    return top


def priority_queue(value_list: dict):
    """
    Функция сортировка по приоритету методом бинарного дерева
    (динамическое программирование)
    """
    top = find_top(value_list)
    flag, n = True, 0
    while flag:
        """ Проход по дереву с перестановкой по возрастанию.
            Минимальная куча. Возвращает отсортированный
            (изменённый) массив по значению Х в массиве
            вида => array[]['symbol',X]"""
        while n < ((2**top-1)-2**(top-1)):
            for i in range(((2**top-1)-2**(top-1))):
                if value_list[2 * i + 1][-1] > value_list[2 * i + 2][-1]:
                    value_list[2 * i + 1], value_list[2 * i + 2] = value_list[2 * i + 2], value_list[2 * i + 1]
                if value_list[i][-1] > value_list[2 * i + 1][-1]:
                    value_list[i], value_list[2 * i + 1] = value_list[2 * i + 1], value_list[i]
                if value_list[2 * i][-1] > value_list[2 * i + 1][-1]:
                    value_list[2 * i], value_list[2 * i + 1] = value_list[2 * i + 1], value_list[2 * i]
            n += 1
        """ Проверка массива на упорядоченность. Если False, 
            Тогда отправляет массив прохождение еще одной 
            перестановки. И так до полной сортировки."""
        for i in range(1, len(value_list)):
            if value_list[i][-1] >= value_list[i-1][-1]:
                n = 0
                if i == len(value_list) - 1:
                    flag = False
                continue
            else:
                n = 0
                break
    return value_list

def sort_list(list: list):
    n = find_top(list)
    k = 0
    if len(list) == 2 ** n - 1:
        priority_queue(list)
    else:
        for i in range(2 ** (n - 1) - 1, len(list)):
            k += 1
        """ Значение max необходимо для определения дополнительного списка 
            additional,которое присоединяется к основному массиву, чтобы 
            сортировка проводилась с 2^N-1 количеством элементов. Потом 
            additional убирается тз основного списка- """
        max_additional = 0
        for i in range(1, len(list)):
            if list[i][-1] > list[i-1][-1] and list[i][-1] > max_additional:
                max_additional = list[i][-1]
            elif list[i-1][-1] > list[i][-1] and list[i-1][-1] > max_additional:
                max_additional = list[i-1][-1]

        additional = []
        for i in range(((2 ** n - 1) - (2 ** (n - 1) - 1) - k)):
            additional.append(['0', max_additional+1])
        list = list + additional
        [0] * ((2 ** n - 1) - (2 ** (n - 1) - 1) - k)
        priority_queue(list)
        for i in range(len(additional)):
            list.pop()
    return list


text = 'effervescence'
print(sort_list(count_symbol(text)))
# print(priority_queue(count_symbol(text)))