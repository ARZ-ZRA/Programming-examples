# Создайте два валидатора. Первая функция-валидатор должна принимать
# два списка чисел и проверять, образован ли второй список путем
# смещения каждого элемента первого списка на число-константу.
def validator_first(list_1, list_2):
    delta_list_1 = set([abs(item_2 - item_1) for item_1, item_2 in zip(list_1, list_1[1:])])
    delta_list_2 = set([abs(item_2 - item_1) for item_1, item_2 in zip(list_2, list_2[1:])])
    if delta_list_1 == delta_list_2:
        print(f'Offset lists are equal in increments {delta_list_2}')
    else:
        print(f'Offset list arn\'t equal in increments.\n'
              f'Offset first list in increments is {delta_list_1}\n'
              f'Offset second list in increments is {delta_list_2}')

def validator(list_1,list_2):
    if list_2 == [i+(list_2[0]-list_1[0]) for i in list_1]:
        print(f'It\'s a addition method, const = {list_2[0]-list_1[0]}')
    elif list_2 == [i * (list_2[0]/list_1[0]) for i in list_1]:
        print(f'It\'s a multiplication method, const = {(list_2[0] * list_1[0]) / list_1[0]}')
    else:
        print('It\'s lists have not connections')

def validator_1(list_1,list_2):
    if len(set([list_2[i]-list_1[i] for i in range(len(list_1))])) == 1:
        print(f'It\'s a addition method, const = {list_2[0]-list_1[0]}')
    elif len(set([list_2[i]/list_1[i] for i in range(len(list_1))])) == 1:
        print(f'It\'s a multiplication method, const = {(list_2[0] * list_1[0]) / list_1[0]}')
    else:
        print('It\'s lists have not connections')



print(validator_1([1, 2, 3], [2, 3, 4]))
print(validator_1([1, 2, 3], [-9, -8, -7]))
print(validator_1([1, 2, 3], [10, 20, 30]))
print(validator_1([1, 2, 3], [-0.5, -1, -1.5]))
print(validator_1([1, 2, 3], [0, 0, 0]))