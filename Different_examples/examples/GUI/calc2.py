from kivy.app import App
from kivy.config import Config
from kivy.properties import StringProperty
from decimal import Decimal
import math

Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 420)

SIGN_FLAG_1 = ['']
LIST_INPUT_1 = list()  # контейнер для ввода данных
LIST_SIGN = list()  # контейнер для ввода знаков
SIGN_FLAG_2 = ['']
LIST_INPUT_2 = list()
LIST_RESULT = list()  # контейнер для вывода результата



class CalculateApp(App):
    title = 'Калькулятор от ARZ '

    info = StringProperty()  # связка с .kv нижний лэйбл - основной
    info_up = StringProperty()  # связка с .kv верхний лэйбл


    # функция очистки ВСЕГО

    def clear_calc(self):
        SIGN_FLAG_1[0] = ''
        LIST_INPUT_1.clear()
        SIGN_FLAG_2[0] = ''
        LIST_INPUT_2.clear()
        LIST_SIGN.clear()
        LIST_RESULT.clear()

        self.info = '0'
        self.info_up = '0'

    # функция Backspace
    def del_calc(self):

        if bool(LIST_INPUT_1) and not bool(LIST_SIGN) and not bool(LIST_INPUT_2):
            del LIST_INPUT_1[-1]
            if len(LIST_INPUT_1) == 0:
                SIGN_FLAG_1[0] = ''
            self.info = ''.join(SIGN_FLAG_1)+''.join(LIST_INPUT_1)

        elif bool(LIST_INPUT_1) and bool(LIST_SIGN) and not bool(LIST_INPUT_2):
            del LIST_SIGN[-1]

        elif bool(LIST_INPUT_1) and bool(LIST_INPUT_2):
            del LIST_INPUT_2[-1]
            if len(LIST_INPUT_2) == 0:
                SIGN_FLAG_2[0] = ''
            self.info = ''.join(SIGN_FLAG_2) + ''.join(LIST_INPUT_2)

        self.info_up = '{SF1}{IN1} {S} {SF2}{IN2}'.format(SF1=''.join(SIGN_FLAG_1), \
                                                          IN1=''.join(LIST_INPUT_1), \
                                                          S=''.join(LIST_SIGN), \
                                                          SF2=''.join(SIGN_FLAG_2), \
                                                          IN2=''.join(LIST_INPUT_2))

    # функция ввода значения
    def input_value(self, inst):
        if not bool(LIST_SIGN):
            LIST_INPUT_1.append(inst.text)
            self.info = '{SF1}{IN1}'.format(SF1=''.join(SIGN_FLAG_1), \
                                            IN1=''.join(LIST_INPUT_1))
            self.info_up = '{SF1}{IN1}'.format(SF1=''.join(SIGN_FLAG_1), \
                                                                IN1=''.join(LIST_INPUT_1), \
                                                                S=''.join(LIST_SIGN), \
                                                                SF2=''.join(SIGN_FLAG_2), \
                                                                IN2=''.join(LIST_INPUT_2))
        elif bool(LIST_SIGN):
            LIST_INPUT_2.append(inst.text)
            self.info = '{SF2}{IN2}'.format(SF2=''.join(SIGN_FLAG_2), \
                                            IN2=''.join(LIST_INPUT_2))
            self.info_up = '{SF1}{IN1} {S} {SF2}{IN2}'.format(SF1=''.join(SIGN_FLAG_1), \
                                                                IN1=''.join(LIST_INPUT_1), \
                                                                S=''.join(LIST_SIGN), \
                                                                SF2=''.join(SIGN_FLAG_2), \
                                                                IN2=''.join(LIST_INPUT_2))

    # функция ввода знака выражения
    def sign(self, inst):

        if not bool(LIST_SIGN):
            LIST_SIGN.append(inst.text)
        else:
            LIST_SIGN[0] = inst.text

        self.info_up = '{SF1}{IN1} {S}'.format(SF1=''.join(SIGN_FLAG_1), \
                                                                IN1=''.join(LIST_INPUT_1), \
                                                                S=''.join(LIST_SIGN), \
                                                                SF2=''.join(SIGN_FLAG_2), \
                                                                IN2=''.join(LIST_INPUT_2))


    # функция знака перед первым и вторым значениями чисел
    def sign_before_number(self):
        if bool(LIST_INPUT_1) and not bool(LIST_SIGN) and not bool(LIST_INPUT_2):       # условие для заполнения 1го значения
            if SIGN_FLAG_1[0] == '':
                SIGN_FLAG_1[0] = '-'
            else:
                SIGN_FLAG_1[0] = ''
            self.info = '{SF1}{IN1}'.format(SF1=''.join(SIGN_FLAG_1), \
                                            IN1=''.join(LIST_INPUT_1))
            self.info_up = '{SF1}{IN1}'.format(SF1=''.join(SIGN_FLAG_1), \
                                                                IN1=''.join(LIST_INPUT_1), \
                                                                S=''.join(LIST_SIGN), \
                                                                SF2=''.join(SIGN_FLAG_2), \
                                                                IN2=''.join(LIST_INPUT_2))

        if bool(LIST_INPUT_1) and bool(LIST_SIGN) and bool(LIST_INPUT_2):       # условие для заполнения 2го значения

            if SIGN_FLAG_2[0] == '':
                SIGN_FLAG_2[0] = '-'
            else:
                SIGN_FLAG_2[0] = ''

            self.info = '{SF2}{IN2}'.format(SF2=''.join(SIGN_FLAG_2), \
                                                IN2=''.join(LIST_INPUT_2))
            self.info_up = '{SF1}{IN1} {S} {SF2}{IN2}'.format(SF1=''.join(SIGN_FLAG_1), \
                                                                    IN1=''.join(LIST_INPUT_1), \
                                                                    S=''.join(LIST_SIGN), \
                                                                    SF2=''.join(SIGN_FLAG_2), \
                                                                    IN2=''.join(LIST_INPUT_2))

    # функция кнопки равно
    def equals_calc(self, inst):
        if bool(LIST_SIGN):
            if '-' in SIGN_FLAG_1:
                s_a = int(-1)
            else:
                s_a = int(1)
            if '-' in SIGN_FLAG_2:
                s_b = int(-1)
            else:
                s_b = int(1)
            a = Decimal(''.join(LIST_INPUT_1))
            b = Decimal(''.join(LIST_INPUT_2))

            if '+' in LIST_SIGN:  # операция сумирования элементов
                result = s_a*a + s_b*b

            elif '-' in LIST_SIGN:  # операция вычитания элементов
                result = s_a * a - s_b * b

            elif '*' in LIST_SIGN:      # операция произведения элементов
                result = (s_a * a) * (s_b * b)

            elif '/' in LIST_SIGN:      # операция нахождения частного элементов
                result = (s_a * a) / (s_b * b)

            SIGN_FLAG_1[0] = ''
            LIST_INPUT_1.clear()
            LIST_SIGN.clear()
            SIGN_FLAG_2[0] = ''
            LIST_INPUT_2.clear()
            LIST_RESULT.append(str(result))
            LIST_INPUT_1.extend(LIST_RESULT)
            self.info = ''.join(LIST_RESULT)
            LIST_RESULT.clear()

    # функция квадрата числа
    def sqr(self):
        LIST_RESULT.append(str(pow(int(''.join(LIST_INPUT_1)), 2)))
        self.info_up = ''.join(LIST_RESULT)
        LIST_INPUT_1.clear()
        LIST_INPUT_1.extend(LIST_RESULT)
        LIST_RESULT.clear()
        self.info = ''.join(LIST_INPUT_1)

    # функция корня квадратного числа
    def sqrt(self):
        LIST_RESULT.append(str(round(math.sqrt(int(float(''.join(LIST_INPUT_1)))), 5)))
        self.info_up = ''.join(LIST_RESULT)
        LIST_INPUT_1.clear()
        LIST_INPUT_1.extend(LIST_RESULT)
        LIST_RESULT.clear()
        self.info = ''.join(LIST_INPUT_1)
    # функция деления еденицы на число
    def division_on_value(self):
        LIST_RESULT.append(str(round(1 / int(''.join(LIST_INPUT_1)), 10)))
        self.info_up = ''.join(LIST_RESULT)
        LIST_INPUT_1.clear()
        LIST_INPUT_1.extend(LIST_RESULT)
        LIST_RESULT.clear()
        self.info = ''.join(LIST_INPUT_1)
    #пока не проработан
    def percent_valua(self):
        LIST_RESULT.append(str(round(1 / int(''.join(LIST_INPUT_1)), 10)))
        self.info_up = ''.join(LIST_RESULT)
        LIST_INPUT_1.clear()
        LIST_INPUT_1.extend(LIST_RESULT)
        LIST_RESULT.clear()
        self.info = ''.join(LIST_INPUT_1)

if __name__ == '__main__':
    CalculateApp().run()
