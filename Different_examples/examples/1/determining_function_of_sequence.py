#Напишите функцию, которая будет определять, является ли переданная
#ей последовательность линейной, квадратичной или кубической.
# Definition of sequence
def def_sec(func):
    list_1 = list()
    for i in func:
        list_1.append(i)
    n = len(list_1)
    if sum(list_1) == 0.5 * n * (n + 1):
        print(f"It's a generator natural number : {list_1}")
    elif sum(list_1) == (n * (n + 1)*(2 * n + 1)) / 6:
        print(f"It's a generator square number : {list_1}")
    elif sum(list_1) == (0.5 * n * (n + 1)) ** 2:
        print(f"It's a generator cube number : {list_1}")
    else:
        print(f"It's a generator unknown number : {list_1}")


from sequence_generator import *
def_sec(nat_num())
def_sec(cube_num())
def_sec(sqr_num())
def_sec([1,2,7,4,5])
