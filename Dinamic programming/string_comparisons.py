def equal_string(string_1: str, string_2: str):
    """Функция сравнения строк"""
    if len(string_1) != len(string_2):
        return False
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            return False
    return True


def test_func(func):
    print(f'Test OK' if func(str(range(10)), str(range(10))) else 'Test Fail')
    print(f'Test OK' if not func(str(range(10)), str(range(5))) else "Test Fail")
    print('Test OK' if not func('qwer', 'qwet') else "Test fail")


test_func(equal_string)
