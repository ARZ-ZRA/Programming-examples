#Напишите функцию, которая будет принимать число n
#и возвращать количество нулей, стоящих в конце
#факториала этого числа.
from functools import reduce
import re

def fact_(num):
    fact = reduce(lambda x, y: x * y, [i for i in range(1, num + 1)])
    fact = str(fact)
    ft = len([i for i in ''.join(re.findall(r'0+$', fact))])
    print(ft)


fact_(15)
fact_(100)
fact_(1000)