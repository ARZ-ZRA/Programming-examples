"""Проверка корректности скобочной последовательности"""
import push_pop

def is_brace_sequence_correct(string: str):
    """Проверяет корректность скобочной последовательности
    из круглых и квадратных скобок () []
    >>> is_brace_sequence_correct("(([()]))[]")
    True
    >>> is_brace_sequence_correct("([(]")
    False
    >>> is_brace_sequence_correct("(")
    False
    >>> is_brace_sequence_correct("]")
    False
    """
    for i in string:
        if i not in "()[]":
            continue
        if i in "([":
            push_pop.push(i)
        else:
            assert i in ")]", "Ожидалась закрывающая скобка"+str(i)
            if push_pop.is_empty():
                return False
            left = push_pop.pop()
            assert left in "([", "Ожидалась закрывающая скобка"+str(i)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != i:
                return False
    return push_pop.is_empty()



if __name__ == "__main__":
    import doctest
    doctest.testmod()