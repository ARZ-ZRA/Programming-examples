#Напишите функцию, которая будет принимать вложенный
#список и возвращать общее количество чисел в нем.
lt = [[1, 4, 7, [1, 4.2, [1]]], ['s', 'q'], [2, 5, 'r', 7]]

import re
def list_num(list_):
    return len(re.findall('\d+\.\d+|\d+', str(list_)))

print(list_num(lt))

def count_number(lst):
    return sum(count_number(i) if type(i) is list else type(i) in (int, float) for i in lst)
print(count_number(lt))