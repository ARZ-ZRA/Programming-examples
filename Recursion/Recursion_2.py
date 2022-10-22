def recursion_number(n, m, list=None):
    '''Функция для перебора массива чисел всех возможных комбинаций методом рекурсии'''
    list = list or []
    if m == 0:
        print(f'{list}')

    else:
        for i in range(n):
            list.append(i)
            recursion_number(n, m-1, list)
            list.pop()

    # return b

recursion_number(5, 4)

# def test_exam_rec():
#     global b
#     b = 0
#     print('test OK' if 4 == recursion_number(2, 2) else 'test Fail')
#     b = 0
#     print('test OK' if 256 == recursion_number(4, 4) else 'test Fail')

# test_exam_rec()