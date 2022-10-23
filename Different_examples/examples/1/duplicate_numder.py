# Напишите функцию, которая будет принимать список nums,
# содержащий числа в диапазоне от 1 до 100, и возвращать
# отсортированный список чисел, которые в списке nums
# встречались дважды.

from collections import Counter
def duplicate_num(list_mum):
    count_ = dict(Counter(list_mum))
    return sorted({i:count_[i] for i in count_ if count_[i] == 2}) or None

# вторая функция хуже
def duplicate_num_1(list_mum):
    return sorted([n for i, n in enumerate(list_mum) if n in list_mum[i+1:]]) or None

print(duplicate_num([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_num([81, 72, 43, 72, 81, 99, 99, 100, 12, 54, 81]))
print(duplicate_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(duplicate_num_1([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_num_1([81, 72, 43, 72, 81, 99, 99, 100, 12, 54, 81]))
print(duplicate_num_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))