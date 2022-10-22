def reverse_polish_notation(list: list):
    """Обратная польская нотация
    >>> reverse_polish_notation([2, 7, '+', 5, '*'])
    45
    >>> reverse_polish_notation([2, 7, 5, '*', '+'])
    37
    """
    import push_pop

    for i in list:
        if type(i) == int:
            push_pop.push(i)
            # print(i)
        if type(i) == str and i in "+-/*" and not push_pop.is_empty():
            value_2 = push_pop.pop()
            value_1 = push_pop.pop()
            if i == '+':
                rezult = value_1 + value_2
            elif i == '-':
                rezult = value_1 - value_2
            elif i == '*':
                rezult = value_1 * value_2
            elif i == '/':
                rezult = value_1 / value_2
            push_pop.push(rezult)
        else:
            assert "Что-то пошло не так"
    return push_pop.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)