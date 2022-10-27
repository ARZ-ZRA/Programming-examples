import random


coordinates = []
count = 0


def matrix_search_recurrently(matrix, number, i=0):
    """
    Функция поиска равного элемента в массиве.
    Реализована с помощью рекурсии
    """
    global count
    k = 0
    if i < len(matrix[0]):
        while k < len(matrix[0]):
            if number == matrix[i][k]:
                count += 1
                coordinates.append((i, k))
            k += 1
        i += 1
        matrix_search_recurrently(matrix, number, i)

    return matrix, coordinates, count


option_1 = matrix_search_recurrently([[random.randint(10, 50) for i in range(10)] for i in range(20)], 30)


for i in option_1[0]:
    print(i)
print(f'\t Сoordinates conformity= {option_1[1]} \n '
      f'\t The total number of identical = {option_1[2]}')

