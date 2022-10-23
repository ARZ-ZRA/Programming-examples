# Напишите функцию, которая будет принимать два списка чисел (вложенный и обычный)
# и проверять, все ли числа в подсписках вложенного принадлежат множеству чисел
# второго, обычного списка.
def valid_lists(list_nested, list_ordinary):
    list_nested_unique = list()
    list_ordinary_unique = list()
    for i in list_nested:
        for item in i:
            if item not in list_nested_unique:
                list_nested_unique.append(item)
    for i in list_ordinary:
        if i not in list_ordinary_unique:
            list_ordinary_unique.append(i)
    if set(list_nested_unique) == set(list_ordinary_unique):
        print(True)
    else:
        print(False)


valid_lists([[3, 3, 2], [1, 2], [2, 1]], [1, 2, 3])
