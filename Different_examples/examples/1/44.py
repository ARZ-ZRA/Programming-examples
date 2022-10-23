#Напишите функцию, которая будет определять, является ли переданная
#ей последовательность линейной, квадратичной или кубической.
def seq_level(lst):
    d, level = {1: 'Linear', 2: 'Quadratic', 3: 'Cubic'}, 0
    while len(set(lst)) != True:
        lst = [a - b for a, b in zip(lst, lst[1:])]
        level += 1
        print(lst)
    return print(d[level])

s = [1, 2, 3, 4, 5]
l=[3, 6, 10, 15, 21]
j=[4, 14, 40, 88, 164]
seq_level(j)
seq_level(l)
seq_level(s)