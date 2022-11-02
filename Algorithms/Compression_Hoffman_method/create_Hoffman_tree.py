from priority_queue import sort_list
from count_symbols import count_symbol


def create_Hoffman_tree(list: list):
    """
    Функция создания древа (tree) кода символов
    """
    # print(list)
    tree = []
    sum = 0

    def create_tree(sum, x, y):
        """
        Функция создания промежуточного списка с двумя элементами
        """
        value = [x[0], y[0]]
        node = [value, sum]
        return node

    def insert_queue_1option(queue, node):
        """
        Функция вставки промежуточного списка в tree и основной список (массив).
        1й вариант
        """
        list.insert(0, node)
        queue.insert(0, node[0])

    def insert_queue_2option(queue, node):
        """
        Функция вставки промежуточного списка в tree и в основной список (массив)
        2й вариант
        """
        list.insert(1, node)
        queue.insert(0, node[0])

    """
    Операции по формированию структуры древа Хоффмана согласно его алгоритма
    """
    while len(list) > 1:
        if len(list) == 2 or list[0][-1]+list[1][-1] <= list[1][-1]+list[2][-1]:
            x = list.pop(1)
            y = list.pop(0)
            sum = x[-1]+y[-1]
            z = create_tree(sum, x, y)
            insert_queue_1option(tree, z)
            # print(f'1st {sum}')
        # if len(list) == 2 or list[0][-1]+list[1][-1] <= list[1][-1]+list[2][-1]:
        #     y = list.pop(1)
        #     x = list.pop(0)
        #     sum = x[-1] + y[-1]
            # print(f'1st {list}')
            # print(tree)
        else:
            x = list.pop(2)
            y = list.pop(1)
            sum = x[-1] + y[-1]
            # print(f'2nd {sum}')
            # print(tree)
            z = create_tree(sum, x, y)
            insert_queue_2option(tree, z)
        # print(f'List {list}')
        # print(f'Tree {tree}')
    # tree[0][0], tree[0][1] = tree[0][1], tree[0][0]

    return tree[0], sum, list

text = 'effervescence'
list_sort = sort_list(count_symbol(text))
code = create_Hoffman_tree(sort_list(count_symbol(text)))[0]
# print(code)
# for i in create_Hoffman_tree(list_sort)[0]:
#     print(i)

def encode_symbol(code):
    """
    Функция создания таблицы соответствия символ => код
    """
    symbol_dict = {}
    for i in range(len(list_sort)-1, -1, -1):
        symbol_dict[list_sort[i][0]] = None

    # k = 0
    # n = []
    # k = []
    list = []
    print(code)
    def translation_into_code(code):
        """
        Функция записи кода d массив на основании таблицы соответствия
        символ => код
        """
        # print(code)
        # print(f'List = {n}')
        if len(code) > 1:
            for i in range(2):
                # print(i, code[i], len(code))
                # print(f' 1List = {n}')
                if type(code[i]) == str:
                    # print(n)
                    # n.append(list)
                    list.append(str(i))
                    symbol_dict[code[i]] = ''.join(list)
                    # n.append(tuple(list))
                    # list.pop()
                    list.pop()
                else:
                    # a = code.pop(i)
                    list.append(str(i))
                    # print(f' 2List = {n}')
                    translation_into_code(code[i])
                    list.pop()
    translation_into_code(code)
    return symbol_dict


import yaml
def write_code_Hoffman_and_text():
    """
    Создание кодированного текста и запись его в файлы
    """
    create = create_Hoffman_tree(sort_list(count_symbol(text)))[0]
    code = encode_symbol(create)
    with open("code_text.txt", "wt") as file_text:
        for i in text:
            file_text.write(code[i])
    with open("code_Hoffman_tree.yaml", "w") as file_code_tree:
        yaml.dump(create, file_code_tree)
    with open(f"code_symbol.yaml", "w") as file_code_text:
        yaml.dump(code, file_code_text)

write_code_Hoffman_and_text()



