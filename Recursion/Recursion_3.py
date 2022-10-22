def generator_permutation(n:int, m:int=-1, list = None):
    m = n if m == -1 else m
    list = list or []
    if m == 0:
        print(*list, end=',', sep='')
        return
    for i in range(1, n+1):
        if find_number(i, list) == True:
            continue
        list.append(i)
        generator_permutation(n, m-1, list)
        list.pop()

def find_number(x, list):
    flag = False
    if x in list:
        flag = True
    return flag

generator_permutation(5)