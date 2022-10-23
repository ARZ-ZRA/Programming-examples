from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print(self.search_input.text)

    def search_location(self):
        search_url = 'http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=fc8fe51064d68f6e028343378ed03c3f'.format(self.search_input.text)
        # запрос к API
        request = UrlRequest(search_url, self.found_location)# в киви есть пакет работающий с
        # сетью (from kivy.network.urlrequest import UrlRequest) в нем есть класс UrlRequest,
        # который отправляет запросы и принимает ответы, первым параметром передается адрес,
        # вторым метод, который будет вызываться после получения ответа, в этот метод будут
        # переданы два аргумента: сам объект и полученный ответ

    def found_location(self, request, data):
        cities = ['{}({})'.format(d['name'], d['sys']['country']) for d in data['list']]  # обработка ответа API, тут, ответ от сайта приходит в формате json,
        # UrlRequest возращает ответ как словарь, по этой причине мы не создавали json объект

        self.search_results.item_strings = cities  # добавляем в объект ListView
class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()
