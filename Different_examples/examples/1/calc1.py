from kivy.app import App
from kivy.config import Config
from kivy.properties import StringProperty
import re
from decimal import Decimal

Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 420)

LIST_INPUT = list()     # контейнер для ввода данных
LIST_SIGN = list()      # контейнер для ввода знаков
LIST_RESULT = list()    # контейнер для вывода результата
EQUAL_FLAG = [0]        # флаг вторичного нажатия знака равно
SF = ['1']


class CalculApp(App):
    title = 'Калькулятор от ARZ '

    info = StringProperty()         # связка с .kv нижний лэйбл - основной
    info_up = StringProperty()      # связка с .kv верхний лэйбл

    # фунция удаления значения
    def del_calc(self):
        if bool(LIST_INPUT):
            del LIST_INPUT[-1]
        if bool(LIST_RESULT):
            del LIST_RESULT[-1]

        self.info = ''.join(LIST_INPUT)
        self.info_up = ''.join(LIST_RESULT)

    # функция очистки ВСЕГО
    def clear_calc(self):
        LIST_INPUT.clear()
        LIST_SIGN.clear()
        LIST_RESULT.clear()
        EQUAL_FLAG[0] = 0

        self.info = ''.join(LIST_INPUT)
        self.info_up = ''.join(LIST_RESULT)

    # функция ввода значения с внутренней функций dd для обрезания ввода
    # третьего значения на экран
    def input_value(self, inst):
        def dd(list_):
            lis = [i for i in re.split("[1234567890.]", ''.join(list_)) if i != '']
            if len(lis) > 1:
                return True

        if not dd(LIST_RESULT):
            LIST_INPUT.append(inst.text)
            LIST_RESULT.append(inst.text)
            if SF[0] == '-1':
                self.info = '-'+''.join(LIST_INPUT)
                self.info_up = '-'+''.join(LIST_RESULT)
            else:
                self.info = ''.join(LIST_INPUT)
                self.info_up = ''.join(LIST_RESULT)
        print(LIST_INPUT)
        print(LIST_RESULT)

    # функция ввода знака с с внутренней функций dd для обрезания ввода
    # второго знака на экран
    def sign(self, inst):

        def dd(list_):
            lis = [i for i in re.split("[1234567890.]", ''.join(list_)) if i != '']
            if len(lis) >= 1:
                return True

        if not bool(LIST_SIGN):
            LIST_SIGN.append(inst.text)
        else:
            LIST_SIGN[0] = inst.text

        if not dd(LIST_RESULT):
            if '+' in LIST_RESULT or '-' in LIST_RESULT or '*' in LIST_RESULT or '/' in LIST_RESULT:
                LIST_RESULT.pop()

            LIST_INPUT.clear()
            LIST_RESULT.extend(LIST_SIGN)
            EQUAL_FLAG[0] = 0

            if SF[0] == '-1':
                self.info_up = '-' + ''.join(LIST_RESULT)
            else:
                self.info_up = ''.join(LIST_RESULT)

        # промежуточная проверка кода
        print(LIST_INPUT)
        print(LIST_SIGN)
        print(LIST_RESULT)

    # функция обработки и вывода результата
    def equals_calc(self):
        if EQUAL_FLAG[0] == 0:
            #if LIST_RESULT[0] == '-':
               # pass
           # else:
            expression_list = re.split("[+\-*/]", ''.join(LIST_RESULT))
            a = Decimal(expression_list[0])
            b = Decimal(expression_list[1])

            if '+' in re.split("[1234567890]", ''.join(LIST_RESULT)):       # операция сумирования элементов
                result = int(''.join(SF))*a + b
                LIST_INPUT.clear()
                LIST_SIGN.clear()
                LIST_RESULT.clear()
                LIST_RESULT.append(str(result))

            elif '-' in re.split("[1234567890]", ''.join(LIST_RESULT)):     # операция вычитания элементов
                result = int(''.join(SF))*a - b
                LIST_INPUT.clear()
                LIST_SIGN.clear()
                LIST_RESULT.clear()
                LIST_RESULT.append(str(result))

            elif '*' in re.split("[1234567890]", ''.join(LIST_RESULT)):     # операция произведения элементов
                result = int(''.join(SF))*a * b
                LIST_INPUT.clear()
                LIST_SIGN.clear()
                LIST_RESULT.clear()
                LIST_RESULT.append(str(result))

            elif '/' in re.split("[1234567890]", ''.join(LIST_RESULT)):     # операция нахождения частного элементов

                #if a % b == 0:                      # этот отбор для целого вывода значения
                    #result = a // b          # при делении ( без .0 )
                #else:
                result = int(''.join(SF))*a / b

                LIST_INPUT.clear()
                LIST_SIGN.clear()
                LIST_RESULT.clear()
                LIST_RESULT.append(str(result))

        EQUAL_FLAG[0] = 1                   # флаг для реализации поведения по второму нажатию знака =
        SF[0] = '1'

        self.info = ''.join(LIST_RESULT)

    def sign_before_number(self):
        if SF[0] == '1':
            SF[0] = '-1'
        else:
            SF[0] = '1'
        print(SF[0])
        if SF[0] == '-1':
            self.info = '-' + ''.join(LIST_INPUT)
            self.info_up = '-' + ''.join(LIST_RESULT)
        else:
            self.info = ''.join(LIST_INPUT)
            self.info_up = ''.join(LIST_RESULT)
       # self.info_up = "".join(LIST_RESULT)

    print(LIST_SIGN)
    print(LIST_RESULT)
    print(EQUAL_FLAG)


if __name__ == '__main__':
    CalculApp().run()
