from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def bild(self):
        return Button(text = "Кнопка",
                font_size = 30,
                on_press = self.bt_press,
                background_color = [1,0,0,1])
    def bt_press(self,instance):
        print('Кнопка нажата')
        instance.text = 'Я нажата'
if __name__ == '__main__':
    MyApp().run()
