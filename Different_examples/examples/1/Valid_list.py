# Напишите функцию, которая будет принимать два списка чисел (вложенный и обычный)
# и проверять, все ли числа в подсписках вложенного принадлежат множеству чисел
# второго, обычного списка.
def valid_list(list_nested, list_ordinary):
    lt_nes = set([item for i in list_nested for item in i])
    lt_ord = set(list_ordinary)
    if lt_nes == lt_ord:
        return print(True)
    else:
        return print(False)


valid_list([[3, 3, 2], [4, 2], [2, 1]], [1, 2, 3])
