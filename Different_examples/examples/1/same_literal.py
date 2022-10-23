# Напишите функцию, которая будет принимать две строки и
# возвращать строку, состоящую из букв, общих для переданных ей строк.

def same_literal(string_1, string_2):
    return ''.join(set(string_1.lower()) & set(string_2.lower()))


print(same_literal("house", "home"))
print(same_literal("Micky", "mouse"))
print(same_literal("house", "villa"))


def shared_letters(a, b):
    return ''.join(sorted(set(l for l in a.lower() if l in b.lower())))