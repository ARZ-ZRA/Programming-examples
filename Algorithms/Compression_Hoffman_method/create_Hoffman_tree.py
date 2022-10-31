from priority_queue import sort_list
from count_symbols import count_symbol



def create_Hoffman_tree(list: list):
    print(list)
    tree = []
    """ Занесение первых двух элементов в код Хоффмана
        начало
    """
    tree.append(list[0])
    if list[0][-1] == list[1][-1]:
        tree.insert(0, list[1])
    else:
        tree.insert(0, [None, list[0][-1]])
    """
    конец
    """
    for i in range(1, len(list)):

        if list[i][-1] == list[i-1][-1]:
            tree.insert(0, i)


    return tree


print(create_Hoffman_tree(sort_list(count_symbol('effervescence'))))