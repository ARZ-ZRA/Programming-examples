import yaml

with open('code_Hoffman_tree.yaml', 'r') as encode_file:
    encode_data = yaml.safe_load(encode_file)

with open('code_text.txt', 'r') as encode_file:
    encode_text = encode_file.read()

text = ''
def decoder_pro(decoder_tree, encoder_code):
    """
    Мощный декодер для распаковки текста, закодированного
    с помощью кода Хоффмана
    """
    """Переводим строку закодированного текста в список"""
    encode_list =list()
    for i in encode_text:
        encode_list.insert(0, int(i))

    def find_symbol(decoder_tree_value):
        """
        Функция для перебора закодированного текста с параллельной
        записью раскодированного текста в переменную text.
        Функция рекурсивная
        """
        global text

        if len(encode_list) > 0:
            while type(decoder_tree_value) == str:
                text = text + decoder_tree_value
                if not bool(encode_list):
                    return
                decoder_tree_value = decoder_tree[encode_list.pop()]

            value = encode_list.pop()
            find_symbol(decoder_tree_value[value])

    find_symbol(decoder_tree[encode_list.pop()])

    return text

print(decoder_pro(encode_data, encode_text))