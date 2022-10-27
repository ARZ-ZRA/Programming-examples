import random


def matrix_search_not_recurent(matrix, number, *args):
    count = 0
    coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number:
                count += 1
                coordinates.append((i, j))
    return matrix, coordinates, count


option_1 = matrix_search_not_recurent([[random.randint(10, 50) for i in range(10)] for i in range(20)], 30)


for i in option_1[0]:
    print(i)
print(f'\t Сoordinates conformity= {option_1[1]} \n '
      f'\t The total number of identical = {option_1[2]}')

