def check_sorted_array(array, ascending=True):
    flag = True
    s = 2*int(ascending)-1
    for i in range(len(array)-1):
        if s * array[i] > s * array[i+1]:
            flag = False
            break
    return flag

array = [4, 7, 8, 4, 3, 0, 65, 4, 3]
print(check_sorted_array(array))

array1 = [1, 7, 8, 8, 8, 9, 9, 9, 11]
print(check_sorted_array(array1, ascending=False))

array2 = [i for i in range(20,-1)]
print(check_sorted_array(array2, ascending=False))
