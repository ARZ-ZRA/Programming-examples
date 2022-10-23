from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty

Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 370)

list_num = []
list_sign = []
class AddCalcForm(BoxLayout):

    label_s = ObjectProperty()
    info = StringProperty()

    def add_number(self, instance):
        list_num.append(str(instance.text))
        self.info = "".join(list_num)

    def backspace(self):
        del list_num[-1]
        self.info = "".join(list_num)

    def sign(self, instance):
        list_num.append(str(instance.text))
        self.info = "".join(list_num)

    def del_result(self):
        list_num.clear()
        list_sign.clear()
        self.info = "".join(list_num)

    def result(self):
        def split_on(list):
            for i in list:
                if i == '-' or i =='+' or i == '*' or i == '/':
                    list_sign.append(i)
            import re
            return re.split("[+\-*/]", ''.join(list))


        expression_list = split_on(list_num)
        a = expression_list[0]
        b = expression_list[-1]
        if '+' in list_sign:
            result = round((float(a) + float(b)), 2)
            list_num.clear()
            list_num.append(str(result))
        elif '-' in list_sign:
            result = round((float(a) - float(b)), 2)
            list_num.clear()
            list_num.append(str(result))
        elif '*' in list_sign:
            result = round((float(a) * float(b)), 2)
            list_num.clear()
            list_num.append(str(result))
        elif '/' in list_sign:
            result = round((float(a) / float(b)), 2)
            list_num.clear()
            list_num.append(str(result))
        list_sign.clear()
        #if result == True:
        self.info = str(result)


    def square(self):
        a = float(''.join(list_num))
        result_squre = round(a*a, 2)
        list_num.clear()
        list_num.append(str(result_squre))
        self.info = str(result_squre)


class CalcApp(App):
    title = 'Калькулятор'

    def build(self):
        return AddCalcForm()


if __name__ == '__main__':
    CalcApp().run()
