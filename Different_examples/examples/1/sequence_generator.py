# Generator natural numbers
def nat_num():
    nat_l = list()
    for i in range(1, 10):
        nat_l.append(i)
    return nat_l


# Generator square number
def sqr_num():
    sqr_l = []
    for i in range(1, 10):
        i = i ** 2
        sqr_l.append(i)
    return sqr_l


# Generator cube number
def cube_num():
    cube_l = list()
    for i in range(1, 10):
        i = i ** 3
        cube_l.append(i)
    return cube_l


#print(nat_num())
#print(sqr_num())
#print(cube_num())
