def search_knut_morris_pratt(string: str, substring: str):
    """Алгоритм Кнута-Мориса-Пратта (Матиясевич) по поиску совпадения полстроки в строке О(N)"""
    # Создание массива П из образа подстроки для фиксации равных длин между суффиксами
    # и префиксами подстроки
    p = [0 for i in range(len(substring))]
    i = 0
    j = 1
    while i < len(substring) - 1 and j < len(substring):
        if substring[j] == substring[i]:
            p[j] = i + 1
            i += 1
            j += 1
        elif substring[j] != substring[i] and i == 0:
            p[j] = 0
            j += 1
        else:
            i = p[i - 1]
    # Нахождение подстроки в строке O(m) m - длинна строки
    k = 0
    g = 0
    while k < len(string):
        if string[k] == substring[g]:
            k += 1
            g += 1
            if g == len(substring):
                return True
        elif string[k] != substring[g] and g > 0:
            g = p[g-1]
        else:
            k += 1

    return False



print(search_knut_morris_pratt('abcabeabcabcabdaaa', 'abcabd'))




# while i < len(substring)-1 and j < len(substring):
    #     if substring[j] != substring[i] and i > 0:
    #         i = p[i-1]
    #         if substring[j] != substring[i]:
    #             p[j] = 0
    #             j += 1
    #         else:
    #             p[j] = i + 1
    #             i += 1
    #             j += 1
    #
    #     elif substring[j] != substring[i]:
    #         p[j] = 0
    #         j += 1
    #
    #     else:
    #         p[j] = i + 1
    #         i += 1
    #         j += 1
    #
    # return p
