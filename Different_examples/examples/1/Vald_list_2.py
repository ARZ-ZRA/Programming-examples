# Напишите функцию, которая будет принимать два списка чисел (вложенный и обычный)
# и проверять, все ли числа в подсписках вложенного принадлежат множеству чисел
# второго, обычного списка.
def valid_lists(list_nested, list_ordinary):
    return set(sum(list_nested, [])) == set(list_ordinary)


def valid_set(list_nest, list_ordin):
    return all(set(x).issubset(list_ordin) for x in list_nest)


print(valid_lists([[3, 4, 2], [1, 2], [2, 1]], [1, 2, 3]))
print(valid_set([[3, 3, 2], [1, 2], [2, 1]], [1, 2, 3]))

