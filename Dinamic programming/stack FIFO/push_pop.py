"""
Модуль описывающий структуру данных стек

>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""
_stack = list()


def push(k):
    _stack.append(k)


def pop():
    k = _stack.pop()
    return k


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
