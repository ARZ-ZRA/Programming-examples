list = []
# ls=[]
b=0
def recursion_number(n, m):
    '''Функция для перебора массива чисел всех возможных комбинаций методом рекурсии'''

    if m == 0:
        global b
        b += 1
        print(f'deep{b}')

    else:
        for i in range(n):
            list_1 = []
            list_1.insert(m,i)
            list.extend(list_1)
            print(f'up{list}')
            recursion_number(n, m-1)

    if list:
        list.pop()
        # print(f'de{list}')
    return b

recursion_number(5, 4)

def test_exam_rec():
    global b
    b = 0
    print('test OK' if 4 == recursion_number(2, 2) else 'test Fail')
    b = 0
    print('test OK' if 256 == recursion_number(4, 4) else 'test Fail')

# test_exam_rec()