# Напишите функцию, которая будет принимать список чисел,
# сортировать его и возвращать наибольшую разность между
# соседними числами.
def max_delta_num(list):
    return max([j-i for i, j in zip(sorted(list), sorted(list[1:]))])

def max_delta_num_1(list):
    list.sort()
    return max([j-i for i, j in zip(list, list[1:])])


print(max_delta_num_1([1,56,43,99,22,4000]))