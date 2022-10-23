#Напишите функцию, которая будет принимать число n
#и возвращать количество нулей, стоящих в конце
#факториала этого числа.
def fact_(num):
    fac = 1
    for i in range(1,num+1):
        fac *= i
    ls = []
    for i in reversed(str(fac)):
        if i == '0':
            ls.append(i)
        else:
            break
    print(fac)
    print(len(ls))


fact_(1000)