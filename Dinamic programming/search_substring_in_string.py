# Варианты прямого сравнения строк
def equal_string(string_1: str, string_2: str):
    """Функция сравнения строк"""
    if len(string_1) != len(string_2):
        return False
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            return False
    return True
def search_substring(string: str, substring: str):
    """Наивный поиск подстроки в строке"""
    for i in range(len(string) - len(substring)):
        if equal_string(string[i:i+len(substring)], substring):
            return True

# мой вариант
def search_substring_in_string(string: str, substring: str):
    """Наивный поиск подстроки в строке"""
    flag = False
    for i in range(len(string)):
        m = i
        for j in range(len(substring)):
            if string[m] == substring[j]:
                m += 1
            if m-i == len(substring):
                flag = True
            continue
    return flag

def test_func(func):
    print('Function search_substring')
    print('Test OK' if not search_substring('abafat', 'abz') else 'test Fail')
    print('Test OK' if search_substring('asdfaswerqrfavs', 'qrfav') else 'test Fail')
    print('Function search_substring_in_string')
    print('Test OK' if not search_substring_in_string('abafat', 'abz') else 'test Fail')
    print('Test OK' if search_substring_in_string('asdfaswerqrfavs', 'qrfav') else 'test Fail')


test_func(search_substring_ in_string)
