from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('style.kv')


class Layout(BoxLayout):
    def message(self):
        pass


class MyApp(App):
    def build(self):
        return Layout()


if __name__ == '__main__':
    MyApp().run()
