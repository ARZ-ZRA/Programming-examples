def count_symbol(text: str):
    """
    Функция подсчёта уникальных символов в тексте
    """
    dictionary_symbols = {}
    for i in text:
        if i in dictionary_symbols:
            count = dictionary_symbols[i]
            count += 1
            dictionary_symbols[i] = count
        else:
            dictionary_symbols[i] = 1
    if not bool(dictionary_symbols):
        print("Dict is empty")
        return
    value_list = list(dictionary_symbols.items())
    for i in range(len(value_list)):
        value_list[i] = list(value_list[i])

    return value_list

# text = 'effervescence'
# print(count_symbol(text))