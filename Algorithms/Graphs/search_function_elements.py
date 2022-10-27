def create_new_array():
    return list()


def insert_list_node(array: list, node: int, node_next: int):

    if bool(array):
        if (node == None or node <= len(array)) and node_next <= len(array):
            value = array[node_next]
            if node == None:
                array.insert(0, value)
            else:
                array.insert(node+1, value)
        else:
            print(f'Index out of array')


def insert_in_list(array: list, node:int, value):

    if bool(array):
        if node == None or node <= len(array):
            if node == None:
                array.insert(0, value)
            else:
                array.insert(node + 1, value)
        else:
            print(f'Index out of array')


def remove_list_node(array: list, )


array = [i**2 for i in range(10)]
print(array)
insert_list_node(array, None, 5)
insert_in_list(array, None, 100)
insert_in_list(array, 40, 140)
insert_in_list(array, 3, 400)
print(array)

def create_new_array():
    return list()


def insert_list_node(array: list, node: int, node_next:int):
    if node == None:
        n = 0
        for i, j in array:
            if j == node_next:
                node_next = array[n]
                n += 1
                break
            n += 1
        array.insert(0, node_next)
        del array[n]
    if bool(array):
        flag_1 = False
        flag_2 = False
        n = 0
        for i, j in array:
            if j == node and not flag_1:
                node, n_node, flag_1 = array[n], n, True

            elif j == node_next and not flag_2:
                node_next, n_node_next, flag_2= array[n], n, True
            n += 1
        if flag_1 and flag_2:
            array.insert(n_node+1, node_next)
            del array[n_node_next]
        else:
            print(f'Input data not in list')
            return


def insert_in_list(array: list, node:int, data):
    flag = False
    n = 0
    for i, j in array:
        if j == node and not flag:
            array[n+1][0], flag = data, True
            break
        n += 1



array = [[7, 3], [3, 1], [1, None], [8, 2], [2, None]]
insert_in_list(array, 3, 20)
print(array)


def create_new_array():
    return list()

def insert_list_node(array: list, node: int, node_next:int):
    if bool(array):
        for i in range(len(array)):
            if array[i][0] == node:
                if array[i][1] == None:
                    array[i][-1] = node_next
                    array.append([node_next, None])
                    print(f'\nFirst condition 1\n')
                    print(f'add {array[i]}')
                    print(array)
                else:
                    array.insert(i+1, [node, node_next])
                    print(f'\nFirst condition 2\n')
                    print(f'add {array[i+1]}')
                    print(array)
                return

        array.append([node, node_next])
        array.append([node_next, None])

        print(f'\nSecond condition\n')
        print(f'add {array[-2], array[-1]}')
        print(array)

    else:
        array.insert(-1, [node, node_next])
        array.append([node_next, None])
        print(f'\nThird condition\n')
        print(f'add {array[-2], array[-1]}')
        print(array)


array = create_new_array()
insert_list_node(array, 7, 3)
insert_list_node(array, 3, 1)
insert_list_node(array, 8, 2)
insert_list_node(array, 3, 8)
insert_list_node(array, 8, 1)
print(array)
