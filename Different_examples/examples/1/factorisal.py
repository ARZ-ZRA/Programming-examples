#Напишите функцию, которая будет принимать число n
#и возвращать количество нулей, стоящих в конце
#факториала этого числа.
import re


def fact_(num):
    p = 1
    for i in range(1, num + 1):
        p *= i
    p = str(p)
    q = len([i for i in ''.join(re.findall(r'0+$', p))])
    print(p)
    print(q)

fact_(5)
fact_(14)
fact_(15)
fact_(50)
